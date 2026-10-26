% Facts
diet(diabetes, 'Low sugar and high fiber food').
diet(obesity, 'Low fat and low calorie food').
diet(anemia, 'Iron rich foods like spinach').
diet(hypertension, 'Low salt and low fat food').
diet(weakness, 'Protein rich food and fruits').

% Rule
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).

% Query
% ?- suggest_diet(diabetes, X).
% ?- suggest_diet(obesity, X).
% ?- suggest_diet(anemia, X).
% ?- suggest_diet(hypertension, X).
