# app/blueprints/preprocessing/routes.py

from flask import Blueprint, render_template, request, redirect, flash, session
import pandas as pd
from app.utils.explanation_engine import explain_preprocessing_step

preprocessing_bp = Blueprint('preprocessing', __name__)

@preprocessing_bp.route('/', methods=['GET', 'POST'])
def upload_and_preview():
    if request.method == 'POST':
        file = request.files.get('dataset')
        if not file or file.filename == '':
            flash('No file selected.')
            return redirect(request.url)

        try:
            df = pd.read_csv(file)
        except Exception as e:
            flash(f'Error reading CSV: {str(e)}')
            return redirect(request.url)

        session['df'] = df.to_json()  # Store in session
        return redirect('/preprocessing/step/1')

    return render_template('upload.html')


@preprocessing_bp.route('/step/<int:step_id>')
def preprocessing_step(step_id):
    if 'df' not in session:
        flash('No dataset uploaded.')
        return redirect('/preprocessing')

    df = pd.read_json(session['df'])

    # 👇 Add new steps here as needed
    steps = ['missing_values', 'categorical_encoding', 'scaling']

    if step_id > len(steps):
        return "Preprocessing complete!", 200

    step_name = steps[step_id - 1]
    explanation = explain_preprocessing_step(df, step=step_name)
    preview_html = df.head().to_html(classes='table table-bordered', index=False)

    next_step = step_id + 1 if step_id < len(steps) else None

    return render_template(
        'preprocessing_steps.html',
        preview=preview_html,
        explanation=explanation,
        next_step=next_step
    )
