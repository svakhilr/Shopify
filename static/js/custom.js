
// [...document.getElementsByClassName('addtoCart')].forEach(function (e){
//     e.addEventListener('click', function(){
//         id = Number(this.getAttribute('value'))
//         var prod_id= $(this).closest('.productdata').find('.prod_id').val();
//         var token = $('input[name=csrfmiddlewaretoken]').val();
//         var var_id= $(this).closest('.productdata').find('.prodvaration').val();
        
        
//         console.log(prod_id)
//         console.log(token)
//         console.log(var_id)
//         $.ajax({
            
//             url:'/cart/addtocart/',
//             method:'POST',
//             dataType: 'json',
//             data: {
//                 "prod_id":prod_id,
//                 "var_id":var_id,
//                 csrfmiddlewaretoken:token
//             },
//             success:(response) => {
//                 console.log(response)
//                 if (response.flag == 4){
//                     swal("Alert!", "Choose Size", "error");
//                 }
//                 else if (response.flag == 1){
//                     swal("Sorry!", "Already Added", "error");
//                 }
//                 else if(response.flag == 2){
//                     swal("Successful!", "Added to Cart", "success");
//                 }

//                 else if(response.flag == 3){
//                     swal("Alert!", "Not Authenticated Login First", "error");
//                 }
//             }
//         })
//     })
// })





