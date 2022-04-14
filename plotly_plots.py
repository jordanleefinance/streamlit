voluntary_labels = labels
mandatory_labels = labels

if health_plan == "Optima Health POS + FSA" or health_plan == "Optima Equity HDHP + FSA":
    if den_plan != "None" and vis_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", den_plan, vis_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3], df_annual.index[4]])
        voluntary_labels = voluntary_labels[1:5]
        mandatory_labels = mandatory_labels[5:]

    elif den_plan == "None" and vis_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", vis_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
        voluntary_labels = voluntary_labels[1:4]
        mandatory_labels = mandatory_labels[4:]

    elif vis_plan == "None" and den_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", den_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
        voluntary_labels = voluntary_labels[1:4]
        mandatory_labels = mandatory_labels[4:]

    elif den_plan == "None" and vis_plan == "None":
        fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)"], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2]])
        voluntary_labels = voluntary_labels[1:3]
        mandatory_labels = mandatory_labels[3:]

if health_plan == "Optima Equity HDHP + HSA":
    if den_plan != "None" and vis_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", den_plan, vis_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3], df_annual.index[4]])
        voluntary_labels = voluntary_labels[1:5]
        mandatory_labels = mandatory_labels[5:]

    elif den_plan == "None" and vis_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", vis_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
        voluntary_labels = voluntary_labels[1:4]
        mandatory_labels = mandatory_labels[4:]

    elif vis_plan == "None" and den_plan != "None":
        fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", den_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
        voluntary_labels = voluntary_labels[1:4]
        mandatory_labels = mandatory_labels[4:]

    elif den_plan == "None" and vis_plan == "None":
        fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)"], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2]])
        voluntary_labels = voluntary_labels[1:3]
        mandatory_labels = mandatory_labels[3:]
if health_plan == 'Optima Equity HDHP' or health_plan == 'Optima Health POS':
    try:
        fig_df = df_annual.loc[[health_plan, den_plan, vis_plan], :]
        new_df = df_annual.drop(
            [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
        voluntary_labels = voluntary_labels[1:4]
        mandatory_labels = mandatory_labels[4:]
    except KeyError:
        pass
    if den_plan == "None" and vis_plan != "None":
        fig_df = df_annual.loc[[health_plan, vis_plan], :]
        new_df = df_annual.drop([df_annual.index[0], health_plan, vis_plan])
        voluntary_labels = voluntary_labels[1:3]
        mandatory_labels = mandatory_labels[3:]
    elif vis_plan == "None" and den_plan != "None":
        fig_df = df_annual.loc[[health_plan, den_plan], :]
        new_df = df_annual.drop([df_annual.index[0], health_plan, den_plan])
        voluntary_labels = voluntary_labels[1:3]
        mandatory_labels = mandatory_labels[3:]

if den_plan == "None" and vis_plan == "None" and health_plan != "Optima Health POS + FSA" and \
        health_plan != "Optima Equity HDHP + FSA" and health_plan != 'Optima Equity HDHP + HSA' \
        and health_plan != "None":
    fig_df = df_annual.loc[[health_plan], :]
    new_df = df_annual.drop([df_annual.index[0], df_annual.index[1]])
    voluntary_labels = voluntary_labels[1:2]
    mandatory_labels = mandatory_labels[2:]

if health_plan == "None" and den_plan != "None" and vis_plan != "None":
    fig_df = df_annual.loc[[den_plan, vis_plan], :]
    new_df = df_annual.drop([df_annual.index[0], df_annual.index[1], df_annual.index[2]])
    voluntary_labels = voluntary_labels[1:3]
    mandatory_labels = mandatory_labels[3:]

if health_plan == "None" and den_plan != "None" and vis_plan == "None":
    fig_df = df_annual.loc[[den_plan], :]
    new_df = df_annual.drop([df_annual.index[0], df_annual.index[1]])
    voluntary_labels = voluntary_labels[1:2]
    mandatory_labels = mandatory_labels[2:]

if health_plan == "None" and den_plan == "None" and vis_plan != "None":
    fig_df = df_annual.loc[[vis_plan], :]
    new_df = df_annual.drop(["Annual Salary", vis_plan])
    voluntary_labels = voluntary_labels[1:2]
    mandatory_labels = mandatory_labels[2:]

if health_plan == "None" and den_plan == "None" and vis_plan == "None":
    fig_df = df_annual
    new_df = df_annual.drop([df_annual.index[0]])
    voluntary_labels = voluntary_labels
    mandatory_labels = mandatory_labels[1:]
plots = make_subplots(
        rows=2, cols=2,
        specs=[[{"colspan": 2, "type": "pie"}, None],
               [{"type": "pie"}, {"type": "pie"}]],

        subplot_titles=("Full Compensation Package", "Voluntary Benefits", "Mandatory Benefits"),
        vertical_spacing=0.35, column_widths=[0.5, 0.5], row_heights=[0.47, 0.53]
    )
    plots.add_trace(
        go.Pie(values=df_annual['Annual Compensation Package'], labels=labels,
               pull=[i for i in explode[:len(labels)]],
               hovertemplate='%{label}: %{value:$,.2f}<extra></extra>\t | \t%{percent}'),
        row=1, col=1

    )

    plots.add_trace(
        go.Pie(values=fig_df['Annual Compensation Package'], labels=voluntary_labels,
               hovertemplate='%{label}: %{value:$,.2f}<extra></extra>\t | \t%{percent}'),
        row=2, col=1

    )

    plots.add_trace(
        go.Pie(values=new_df['Annual Compensation Package'], labels=mandatory_labels,
               hovertemplate='%{label}: %{value:$,.2f}<extra></extra>\t | \t%{percent}'),
        row=2, col=2

    )
    plots.update_layout(height=700, width=1500, legend_title="Legend", legend_font_size=14,
                        legend_title_font_size=19, legend=dict(orientation="v", x=1.25))
    plots.update_traces(textposition='inside', textinfo='percent+label')

    plots.data[0].domain = {'x': [0.08, 0.98], 'y': [0.45, 0.98]}