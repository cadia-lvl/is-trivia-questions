## Notes on data cleanup 

* The data is normalized using a (Grammateks fork of Regin Normalizer)[https://github.com/grammatek/regina_normalizer]. The fork is modified and special TTS addition where commmented out 
* Questions_sorted_filtered 
  * It's the output from Regina
  * The tag `<sil>` appears in the normalized text when there is a `-`. I removed the tag or often the entire sentence.
  * All questions with the tag `Stærðfræði` where removed.
  * Removed alot of sentence with the tags `eðlisfræði` or `efnafræði` for the same reason as for `stærðfræði`. Equations are not handled in Regina. 
  * 
