$(document).ready(function () {
    // Init
    var table;
    $('#table_search').hide();
    $('#on-loading').hide();
    $("body").css({"background-image":"url()"});
    // searh
    $('#btn-search').click(function () {
        $('#table_search').hide();
        $('#on-loading').show();

        var data ={};
        data['content']=$('#input-search').val();
        if (data['content']!="") {
             $("#search-head").css("margin-top",2+"%");
            console.log(data);
            $.getJSON({
                type: 'POST',
                url: '/searchContent',
                data: JSON.stringify(data),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',

                success: function (data) {
                    $('#on-loading').hide();
                    $('#table_search').show();
                    table = $('#table_search').DataTable({
                        destroy: true,
                        fixedHeader: true,
                        processing: true,
                        responsive: true,
                        "ordering": false,
                        searching: false,
                        lengthChange: false,
                        "lengthMenu": [25],
                        data: data,
                        columns: [
                            {data: 'title'},
                            {data: 'page'}
                        ]
                    });


                },
            });
        }
         else
        {
            $('#on-loading').hide();
        }
    });


    $('#input-search').bind('keypress',function(event){
        if(event.keyCode == "13") {
            $('#table_search').hide();
             $('#on-loading').show();

        var data ={};
        data['content'] = $('#input-search').val();
        if (data['content']!="") {
            $("#search-head").css("margin-top",2+"%");
            console.log(data);
            $.getJSON({
                type: 'POST',
                url: '/searchContent',
                data: JSON.stringify(data),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',

                success: function (data) {
                    $('#on-loading').hide();
                    $('#table_search').show();
                    table = $('#table_search').DataTable({
                        destroy: true,
                        fixedHeader: true,
                        processing: true,
                        responsive: true,
                        "ordering": false,
                        searching: false,
                        lengthChange: false,
                        "lengthMenu": [25],
                        data: data,
                        columns: [
                            {data: 'title'},
                            {data: 'page'}
                        ]
                    });


                },
            });
        }
        else
        {
            $('#on-loading').hide();
        }
        }
    });


    $("#table_search").on("click","tr",function(){//给tr或者td添加click事件

      var data=table.row(this).data();//获取值的对象数据
      $.alert({
        columnClass: 'col-md-8',
        theme:'material',
        title: data.title,
        content:''+
        '<p><b>Authors:</b><br>'+
            data.authors+
        '</p>'+
        '<p><b>Abstract:</b><br>'+
        '<p style="text-indent:2em">'+
        data.abstract+
        '</p>'+
        '</p>',
        draggable: true,
        buttons: {


            GoPDF: {
                btnClass: 'btn-green',
                text: 'go to pdf',
                action: function () {
                    var pdfurl=data.page.split('abs');//某一行中要是用的表头值
                    window.open(pdfurl[0]+'pdf'+pdfurl[1]+'.pdf');
                }
            },

           cancel: {
                btnClass: 'btn-blue',
                action:function () {

            }
            }
    }
        });
    });


});
