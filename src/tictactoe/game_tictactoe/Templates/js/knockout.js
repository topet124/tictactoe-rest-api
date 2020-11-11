function AppViewModel() {
  var self = this;

self.temitope  = ko.observable();

  self.board  = ko.observableArray(['0','1','2',
               '3','4','5',
               '6','7','8'
  ])
  self.getStarted = function() {
      $.ajax({
          type: 'POST',
          url: '/tic',
          beforeSend: function(request) {
            request.setRequestHeader("X-CSRFToken", csrftoken);
            },
            dataType: 'json',
          data: ko.toJSON({
            value : self.temitope(),
            x : self.board()
          })
      })

      .done(function(result) {
        self.board.removeAll();
        self.temitope(null);
          if(result.winner == 'o'){
            alert('O wins');
            location.reload();
          }else if (result.winner == 'x'){
            alert('X wins');
            location.reload();
          }else if(result.taken == 'taken'){
            alert('result.taken');
            self.board(result.board);
            return true;
          }else{
            self.board(result.board);
            console.log(self.board());
          }
      })

      .fail(function(xhr, status, error) {
          console.log(error);
          console.log(xhr);
          console.log(status);
      })

      .always(function(data){
      });
  }


}
    $(document).ready(function () {
        $.ajaxSetup({ cache: false });
        ko.applyBindings(new AppViewModel(), document.getElementById('loader'));
    });