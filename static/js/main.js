
// Main JS code
// -------------------------------------------------------------------------------

// Loader on and off:
$(document).on('click', 'a', function(event) {  if ( event.ctrlKey ) { } else { $('.loader').show(); } });
$(document).ajaxStart(function(){$('.loader').show();});
$(document).ajaxComplete(function(){$('.loader').delay(5000).hide();});
$(document).ready(function(){ $('.loader').delay(5000).hide(); });
$(document).on('click', '.hide-loader', function() { $('.loader').delay(50000).hide(); });


//get week number function
Date.prototype.getWeek = function () { 
    var date = new Date(this);
    return $.datepicker.iso8601Week(date); 
}

// Tabs
function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("content-tab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" is-active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " is-active";

    evt.stopImmediatePropagation()
    $('.loader').hide();
  }


// add Variable
$(document).on('click', '#add_variable', function() {
    var u_id = $('#usecase').attr('u_id')

    $.ajax({
        url: '/usecase/' + u_id + '/variable/new',
        success: function (data) {
            floater_open(data)
         }
     });
 });


// update Variable
$(document).on('click', '.variable', function() {
    var u_id = $('#usecase').attr('u_id')
    var v_id = $(this).attr('v_id')

    $.ajax({
        url: '/usecase/' + u_id + '/variable/' + v_id,
        success: function (data) {
            floater_open(data)
            variable_form_change($('#id_variable').find(":selected").val())
        }
    });
});


// Variable function change
$(document).on('change', '#id_variable', function() {
    variable = $(this).find(":selected").val()
    variable_form_change(variable)
});

function variable_form_change(variable){
    initial_func = $('#id_function').find(":selected").val()
    allowed = allowed_functions[variable]
    // Hide all options
    $("#id_function > option").each(function() {  $(this).css('display','none')} )
    // show allowed
    $.each(allowed, function(i,f){
        $('#id_function').children('option[value="' + f + '"]').css('display','block')
        }
    )

    // update function field
    if (allowed.includes(initial_func)) { func = initial_func} else {func = allowed[0]}
    $('#id_function').children('option[value="' + func + '"]').prop("selected", true);
    variable_form_function_change(func)
}


// Variable function change
$(document).on('change', '#id_function', function() {
    func = $(this).find(":selected").val()
    variable_form_function_change(func)
});

function variable_form_function_change(func){
    if ( func == 'spread') { 
        $('#form_array').fadeOut(0)
        $("#form_end_date #id_end_date").val('').prop('disabled', true);
        $('#form_start_point > div > label').text('Value')
        $('#form_end_point > div > label').text('Period')
        $('#form_end_point, form_start_point').fadeIn(0)
        $('#form_start_point').attr('colspan',1);
        $('#form_points').fadeIn(0) 
    }
    else if ( ['constant','add','multiply'].includes(func)) {
        $('#form_array').fadeOut(0) 
        $('#form_end_point').fadeOut(0)
        $("#form_end_date #id_end_date").prop('disabled', false);
        $('#form_start_point > div > label').text('Constant')
        $('#form_start_point').attr('colspan',2);
        $('#form_start_point').fadeIn(0) 
        $('#form_points').fadeIn(0) 
    }
    else if ( ['linear','exponential','logarithmic'].includes(func)) {
        $('#form_array').fadeOut(0) 
        $("#form_end_date #id_end_date").prop('disabled', false);
        $('#form_start_point > div > label').text('Start Point')
        $('#form_end_point > div > label').text('End Point')
        $('#form_end_point, form_start_point').fadeIn(0)
        $('#form_start_point').attr('colspan',1);
        $('#form_points').fadeIn(0) 
    }
    else if ( func == 'array') { 
        $('#form_points').fadeOut(0)
        $("#form_end_date #id_end_date").val('').prop('disabled', true);
        $('#form_array').fadeIn(0)
    }
}


// submit vairble
$(document).on('click', '#variable_form_submit', function(e){
    e.preventDefault()
    var u_id = $('#usecase').attr('u_id')
    formdata = $('#variable_form').serialize() + '&v_id=' + $('#variable_form').attr('v_id');

    $.ajax({
        type : "POST",
        url: '/usecase/' + u_id + '/variable/submit',
        data: formdata,
        success: function (formdata) {
            location.reload();
            },
        async: false,
    });
});


// delete vairble
$(document).on('click', '#variable_form_delete', function() {
    var u_id = $('#usecase').attr('u_id')
    var v_id = $('#variable_form').attr('v_id');

    if (confirm('Are you sure, you would like to delete this variable?')) {
        $.ajax({
            type : "GET",
            url: "/usecase/" + u_id + "/variable/" + v_id + "/delete",
            success: function () {
                floater_close();
                location.reload();
                },
            async: false,
        });
    }
});
              

// Usecase Retiered Filter 
// ----------------------------------------------------------------------------

$(document).on('click', '#show_retired', function() {
    $('.loader').show(); 
    
    // reset link
    link =  window.location.href.replace('retired=true','')

    // add remove filter
    if($(this).is(":checked")) {
        if (link.indexOf('?') > -1)
            {link += '&' + 'retired=true'}
        else
            {link += '?' + 'retired=true'}
    } 

    window.location.href = link
});


// Research Calc Vals
// ----------------------------------------------------------------------------

$(document).on('click', '#show_exploratory', function() {
    $('.loader').show(); 
    
    // reset link
    link =  window.location.href.replace('exploratory=true','')

    // add remove filter
    if($(this).is(":checked")) {
        if (link.indexOf('?') > -1)
            {link += '&' + 'exploratory=true'}
        else
            {link += '?' + 'exploratory=true'}
    } 

    window.location.href = link
});

// Report Show Exploratory 
// ----------------------------------------------------------------------------

$(document).on('click', '#show_exploratory', function() {
    $('.loader').show(); 
    
    // reset link
    link =  window.location.href.replace('exploratory=true','')

    // add remove filter
    if($(this).is(":checked")) {
        if (link.indexOf('?') > -1)
            {link += '&' + 'exploratory=true'}
        else
            {link += '?' + 'exploratory=true'}
    } 

    window.location.href = link
});

// Report filter
// ----------------------------------------------------------------------------

function apply_report_filter(type, monthly=false) {
    var d_id = $('#disease').attr('d_id')
    url = '/disease/' + d_id

    if (type=='report'){
        var r_id = $('#report').attr('r_id')
        var s_id = $('#section').attr('s_id')
        var t_id = $('#table').attr('t_id')
        var scn = $('#scenario').attr('scn_code')
        url += '/report/' + r_id + '/' + scn + '/details/' + s_id + '/' + t_id
        if ($('#filter_date').val() != "" ){ url += '?start_date=' + $('#filter_date').val()}


    } else if (type=='assessment'){
        var s_id = $('#scenario').attr('s_id')
        url += '/analysis/' + type + '/' + s_id + '/view'
        if ($('#filter_field').find(':selected').val() != 0 ){ url += '/' + $('#filter_field').find(':selected').val()}
        if ($('#filter_date').val() != "" ){ url += '?start_date=' + $('#filter_date').val()}

    } else {
        url += '/analysis/' + type + '/view'
        if ($('#filter_field').find(':selected').val() != 0 ){ url += '/' + $('#filter_field').find(':selected').val()}
        if (monthly == 'True'){ url += '?stdm_mon=true&'} else {url += '?stdm_mon=false&'}
        if ($('#filter_date').val() != "" ){ url += '?start_date=' + $('#filter_date').val()}

    }

    // add date filte=r - has to be at the end
    window.location.href =  url
};


function apply_download_button(type, monthly=false) {
    var d_id = $('#disease').attr('d_id')
    url = '/disease/' + d_id

    if (type=='report'){
        var r_id = $('#report').attr('r_id')
        var s_id = $('#scenario').attr('s_id')
        var c_id = $('#chart').attr('c_id')
        url += '/report/' + r_id + '/details/' + s_id + '/' + c_id

    } else if (type=='symp'){
        url += '/analysis/' + type + '/extract'
        if ($('#filter_field').find(':selected').val() != 0 ){ url += '/' + $('#filter_field').find(':selected').val()}
        if (monthly == 'True'){ url += '?stdm_mon=true&'} else {url += '?stdm_mon=false&'}

    } else if (type=='assessment'){
        var s_id = $('#scenario').attr('s_id')
        url += '/analysis/' + type + '/' + s_id + '/extract'
        if ($('#filter_field').find(':selected').val() != 0 ){ url += '/' + $('#filter_field').find(':selected').val()}
        if ($('#filter_date').val() != "" ){ url += '?start_date=' + $('#filter_date').val()}

    } else {
        url += '/analysis/' + type + '/extract'
        if ($('#filter_field').find(':selected').val() != 0 ){ url += '/' + $('#filter_field').find(':selected').val()}
    }

    // add date filte=r - has to be at the end
    if ($('#filter_date').val() != "" ){ url += '?start_date=' + $('#filter_date').val()}

    window.location.href =  url
};

// Group Management 
// ----------------------------------------------------------------------------

// add group
$(document).on('click', '#add_group', function() {
    var d_id = $('#disease').attr('d_id')

    $.ajax({
        url: '/disease/' + d_id + '/group/new',
        success: function (data) {
            floater_open(data)
         }
     });
 });


// update group
$(document).on('click', '.group', function() {
    var d_id = $('#disease').attr('d_id')
    var g_id = $(this).attr('g_id')

    $.ajax({
        url: '/disease/' + d_id + '/group/' + g_id,
        success: function (data) {
            floater_open(data)
        }
    });
});


// submit group
$(document).on('click', '#group_form_submit', function(e){
    e.preventDefault()
    var d_id = $('#disease').attr('d_id')
    formdata = $('#group_form').serialize() + '&g_id=' + $('#group_form').attr('g_id');

    $.ajax({
        type : "POST",
        url: '/disease/' + d_id + '/group/submit',
        data: formdata,
        success: function (formdata) {
            location.reload();
            },
        async: false,
    });
});


// delete group
$(document).on('click', '#group_form_delete', function() {
    var d_id = $('#group').attr('d_id')
    var g_id = $('#group_form').attr('g_id');

    if (confirm('Are you sure, you would like to delete this group?')) {
        $.ajax({
            type : "GET",
            url: "/disease/" + d_id + "/group/" + g_id + "/delete",
            success: function () {
                floater_close();
                location.reload();
                },
            async: false,
        });
    }
});

// Report 
// ----------------------------------------------------------------------------

// get report [latest] - main screen buttons
function get_report(type){
    $('.loader').show();

    // disease
    var disease_id = $('#disease').attr('d_id')
    
    // scenario
    var scn_code
    $(".rep_scenario input[type=checkbox]").each(
        function() { if($(this).is(":checked")) { scn_code = $(this).attr('scn_code') } }
    );

    // options 
    options = '?'
    $(".rep_option input[type=checkbox]").each(
        function() { 
            options += '&'
            if($(this).is(":checked")) { options += $(this).attr('name') + '=true' } else { options += $(this).attr('name') + '=false'}
        }
    );

    // get the report
    if (type != 'assessment') {
        window.location.href = '/disease/' + disease_id + '/report/latest/'+ scn_code + '/' + type + options;
    } else {
        window.location.href = '/disease/' + disease_id + '/analysis/assessment/'+ scn_code + '/view';
    }
}   


function get_symp(){

    var disease_id = $('#disease').attr('d_id')

    // options 
    options = '?'
    $(".symp_option input[type=checkbox]").each(
        function() { 
            options += '&'
            if($(this).is(":checked")) { options += $(this).attr('name') + '=true' } else { options += $(this).attr('name') + '=false'}
        }
    );

    window.location.href = '/disease/' + disease_id + '/analysis/symp/view' + options;

}

// view report data extract
function report_data_extract_form(rep_id) {
    var d_id = $('#disease').attr('d_id')

    $.ajax({
        url: '/disease/' + d_id + '/report/' + rep_id + '/extract/form',
        success: function (data) {
            floater_open(data)
        }
    });
}

// get report data extract file
function report_get_data_extract(rep_id) {
    var d_id = $('#disease').attr('d_id')
    var section = $('#report_extract_section').val()
    var table = $('#report_extract_table').val()
    
    link = '/disease/' + d_id + '/report/' + rep_id + '/extract/' + section + '/' + table,
    window.location.href = link
}



// Commnet eid/new
$(document).on('click', '.r_comment', function() {
    var r_gen = $(this).attr('r_gen')
    var scenario = $(this).attr('scenario')
    var chart_id = $(this).attr('chart_id')
    var com_id = $(this).attr('com_id')

    url = '/comment/' + r_gen + '/' + scenario +  '/' + chart_id

    if (com_id) {url += '/' + com_id }

    $.ajax({
        url: url,
        success: function (data) {
            floater_open(data)
         }
     });
 });

// submit comment
$(document).on('click', '#comment_form_submit', function(e){
    e.preventDefault()
    var r_gen = $('#comment_form').attr('r_gen')
    var scenario = $('#comment_form').attr('scenario')
    var chart_id = $('#comment_form').attr('chart_id')
    
    formdata = $('#comment_form').serialize() + '&com_id=' + $('#comment_form').attr('com_id');

    $.ajax({
        type : "POST",
        url: '/comment/' + r_gen + '/' + scenario + '/' + chart_id + '/submit',
        data: formdata,
        success: function (data) {
            data = JSON.parse(data)
            $('#'+chart_id+'_comment_text').show()
            $('#'+chart_id+'_comment_text').css("white-space","pre-line");
            $('#'+chart_id+'_comment_text').html( $('#id_text').val() )
            $('#'+chart_id+'_comment_btn').attr('com_id', data.com_id)
            floater_close();
            },
        async: false,
    });
});


// delete comment
$(document).on('click', '#comment_form_delete', function() {

    var r_gen = $('#comment_form').attr('r_gen')
    var chart_id = $('#comment_form').attr('chart_id')
    var com_id = $('#comment_form').attr('com_id');

    if (confirm('Are you sure, you would like to delete this comment?')) {
        $.ajax({
            type : "GET",
            url: '/comment/' + r_gen + '/' + chart_id + '/' + com_id + "/delete",
            success: function (data) {
                floater_close();
                $('#'+chart_id+'_comment_text').hide()
                $('#'+chart_id+'_comment_text').html('')
                $('#'+chart_id+'_comment_btn').attr('com_id', '')
                },
            async: false,
        });
    }
});
              


// Chart functions 
// ----------------------------------------------------------------------------

// this makes the legend removed once clicekd instead of being hashed
const newLegendClickHandler = function (e, legendItem, legend) {
    //ci is the chart
    const index = legendItem.datasetIndex;
    const ci = legend.chart;

    // save the dataset needing to be removed for alter
    ci.removed_datasets.push(ci.data.datasets[index])

    // remove the data set
    ci.data.datasets.splice(index, 1);
    ci.update();

    //show the reset button
    $('#' + ci.id + '_reset').show()
}

function chart_reset (ci) {
    //ci is the chart
    for (d in ci.removed_datasets){
        ci.data.datasets.push(ci.removed_datasets[d])
        }
        ci.update();

    //hide the reset button
    $('#' + ci.id + '_reset').hide()
}



// Report chart download
function chart_download_as_image(chart) {
    var link = document.createElement('a');
    link.href = chart.toBase64Image();
    link.download = chart.title + '.png';
    link.click();
    chart.options.title.text = chart.title;
    chart.update({duration: 0});
}


// Chart set axis
function set_y_axis(chart, type) {

    if (type == 'log'){
        chart.options.scales.myScale.type='logarithmic'
        chart.update()
    } else {
        chart.options.scales.myScale.type='linear'
        chart.update()
    }

}


// Report chart add exploratory
function chart_include_exploratory(chart) {
    chart.data.labels.push(chart.exploratory['label']);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(chart.exploratory['data']);
    });
    chart.update();
}

// Report chart create details data table
function chart_create_data_table(dataset) {
    var html = '<table class="table has-text-centered is-striped is-fullwidth is-hoverable is-small is-size-7">';
    html += '<thead><tr><th style="width:120px;">Date</th>';
    
    var columnCount = 0;
    jQuery.each(dataset.datasets, function (idx, item) {
        html += '<th style="background-color:' + item.fillColor + ';">' + item.label + '</th>';
        columnCount += 1;
    });

    html += '</tr></thead>';

    jQuery.each(dataset.labels, function (idx, item) {
        html += '<tr><td>' + item + '</td>';
        for (i = 0; i < columnCount; i++) {
            html += '<td style="background-color:' + dataset.datasets[i].fillColor + ';">' + (dataset.datasets[i].data[idx] === '0' ? '-' : dataset.datasets[i].data[idx]) + '</td>';
        }
        html += '</tr>';
    });

    html += '</tr><tbody></table>';

    return html;
};

// view chart table only
 function view_chart_table(chart_id) {
    var d_id = $('#disease').attr('d_id')

    $.ajax({
        url: '/disease/' + d_id + '/report/view_chart_table/' + chart_id,
        success: function (data) {
            floater_open(data)
        }
    });
}


// Research Calc Vals update
// ----------------------------------------------------------------------------

function researchCalcValsUpdate() {
    $('.loader').show();
  
    // reset link
    link = window.location.href.split('?')[0];
    parameters = '?';
  
    // add remove filter
    $('.input').each(function () {
      parameters += '&' + $(this).attr('id') + '=' + $(this).val();
    });
  
    window.location.href = link + parameters;
  }
  
  // Update research calcs on click of calculate button
  $(document).on('click', '#Update_research_calc', function () {
    researchCalcValsUpdate();
  });
  
  // Update research cals on change of population dropdown
  $(document).on('change', '#population_dropdown', function () {
    researchCalcValsUpdate();
  });


// Floater :----------------------------------------------------------------------------------------------------------
function floater_open(data){
    var f_size = data.floater
    var f_id = data.id
    var f_HTML = data.content
    $('.loader').hide();
    $("body").append('<div class="blackout"></div>')
    $("body").append('<div class="floater floater_' + f_size + '" id="' + f_id + '"></div>')
    $(".floater").append(f_HTML)
};

$(document).on('click', '[name="floater_cancel"]', function() { floater_close() });

function floater_close(){
    $('body').removeClass('stop-scrolling')
    $(".floater").fadeOut(300,function(){ $(this).remove();})
    $(".blackout").fadeOut(300,function(){ $(this).remove();})
    $('.loader').hide();
};
