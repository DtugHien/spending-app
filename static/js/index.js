$(document).ready(() => { 
    let new_date = Date.now();
    const beginDate = $('#container-date-beginDate');
    const lastDate = $('#container-date-lastDate');
    const spendOn = $("#container-form-name");
    const currency = $("#container-form-currency");
    const types = $("#container-form-type");
    const typeFilter = $("#container-date-type");
    const cost = $("#container-form-price");
    const detail = $("#container-form-detail");
    const dateWarning = $("#date-warning");
    const filterButton = $("#filter-button");

    lastDate.focusout(async () => {
        if (new Date(lastDate.val()).getTime() - new Date(beginDate.val()).getTime() < 0){
            dateWarning.css("display", "inline");
            lastDate.val(beginDate.val());
        }
        else {
            dateWarning.css("display", "none");
        }
    })

    beginDate.focusout(async () => {
        if (new Date(lastDate.val()).getTime() - new Date(beginDate.val()).getTime() < 0){
            dateWarning.css("display", "inline");
            lastDate.val(beginDate.val());
        }
        else {
            dateWarning.css("display", "none");
        }
    })

    filterButton.click(async () => {
        await $.ajax({
            url: '/filter',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                type: typeFilter.val(),
                begin_time: new Date(beginDate.val()).getTime(),
                last_time: new Date(lastDate.val()).getTime(),
            }),
            type: 'UPDATE',
            success: respone => location.reload(),
            error: error => console.log(error), 
        })
    })

    $('.container-form').submit(async (e) => {
        const time_stamp = Date.now() + 86400000
        e.preventDefault();
        await $.ajax({
            url: '/add',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                spendOn: spendOn.val(),
                currency: currency.val(),
                type: types.val(),
                date: new Date(time_stamp).toLocaleDateString('en-CA'),
                cost: cost.val(),
                detail: detail.val(),
                time_stamp
            }),
            type: 'POST',
            success: respone => location.reload(),
            error: error => console.log(error),
        })
    });
});
