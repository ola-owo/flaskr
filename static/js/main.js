function getLocalTime(dateTimeString){
  var dateTime = new Date( dateTimeString.replace(/-/g, '/') );
  var tzoffset = dateTime.getTimezoneOffset(),
      minuteOffset = tzoffset % 60,
      hourOffset = Math.floor(tzoffset / 60);
  dateTime.setMinutes( dateTime.getMinutes() - minuteOffset );
  dateTime.setHours( dateTime.getHours() - hourOffset );
  return dateTime;
}
$(document).ready(function(){
  $('.flash').slideDown();
  $('.timestamp').hover(function(){
    // change from UTC to local time on hover
    var dateTime = getLocalTime( $(this).parent().attr('data-timestamp') );
    $(this).text( dateTime.toLocaleFormat('%b %d %Y at %I:%M:%S %p (%Z %z)') ); 
  }, function(){
    var utcDateTime = $(this).parent().attr('data-timestamp');
    $(this).text(utcDateTime);
  });

  $('.add-entry').submit(function(){
    // leave no fields unfilled!
    var error = false;
    $('.entry_error').empty();
    if( !$('.add-entry input').val() ){
      $('.entry_title .entry_error').text('You need a title!')
      error = true;
    }
    if( !$('.add-entry textarea').val() ){
      $('.entry_text .entry_error').text('You need a description!')
      error = true;
    }
    if(error){return false}
  });
});