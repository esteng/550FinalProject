#!/usr/bin/gawk -f
#
# This script reads a tab-separated file and syllabifies the columns pointed to by the variable’phons’ (ot the first column, by default).
#
#
# Author: Christophe Pallier (christophe.pallier@m4x.org)
#
# License: GNU (cf. http://www.gnu.org)
#
# Last update: 13 May 2004
# (original date: the first version of this script was written during
# my dissertation, in 1993)
#
# 2004/05/13: merge of the Brulex & Lexique versions
# correction for the ’j’->’Z’ (viellerie) in Lexique
# add rule ’[td]R’ (comment on ’autrefois’ by Sprenger-Charolles) # 2004/04/26: add rule with 5 consonnants (comment on ’exploit’ by J. Goslin)
#
#
#
# Note: changed \377 into y-umlaut to run under DOS (bug gawk).
21
BEGIN {
FS="\t";
OFS="\t";
25
if (code=="brulex") {
V="[aiouyîâêôû^eEéAO_]"; # vowels
C="[ptkbdgfs/vzjmnN£]"; # consonants except liquids & semivowels
C1="[pkbgfs/vzj]";
L="[lR]"; # liquids
Y="[ïü\377]"; # semi-vowels \377 stands for y-umlaut
X="[ptkbdgfs/vzjmnN£xlRïü\377]"; # all consonants
} else { # code == LAIPTTS)
V="[iYeE2591a@oO§uy*]"; # Vowels
C="[pbmfvtdnNkgszxSZGh]"; # Consonants except liquids & semivowels
C1="[pkbgfsSvzZ]";
5
L="[lR]"; # liquids
Y="[j8w]"; # semi-vowels
X="[pbmfvtdnNkgszSZGlRrhxGj8w]"; # all consonants, including semivowels
}
if (phons==0) phons=1;
}
43
{
a=$phons;
n=1
}
48
{
while (i= match (a, V V)) {
a=substr(a,1,i) "-" substr(a,i+1,length(a)); n++; }
52
while (i= match(a, V X V)) {
a=substr(a,1,i) "-" substr(a,i+1,length(a)); n++}
55
while (i=match(a, V Y Y V)) {
a=substr(a,1,i+1) "-" substr(a,i+2, length(a)); n++}
58
while (i=match(a, V C Y V)) {
a=substr(a,1,i) "-" substr(a,i+1, length(a)); n++}
61
while (i=match(a, V L Y V)) {
a=substr(a,1,i) "-" substr(a,i+1, length(a)); n++}
64
while (i=match(a, V "[td]R" V)) {
a=substr(a,1,i) "-" substr(a,i+1, length(a)); n++}
67
while (i=match(a, V "[td]R" Y V)) {
a=substr(a,1,i) "-" substr(a,i+1, length(a)); n++}
70
while (i=match(a, V C1 L V)) {
a=substr(a,1,i) "-" substr (a,i+1,length(a)); n++}
73
while (i=match(a, V X X V)) {
a=substr(a,1,i+1) "-" substr(a,i+2, length(a)); n++}
76
while (i= match(a, V X X X V)) {
a=substr(a,1,i+1) "-" substr(a,i+2,length(a)); n++}
79
while (i=match(a, V X X X X V)) {
a=substr(a,1,i+1) "-" substr(a,i+2,length(a)); n++}
82
while (i=match(a, V X X X X X V)) {
a=substr(a,1,i+1) "-" substr(a,i+2,length(a)); n++}
85
6
# suppress the final schwa (^) in some multisyllabic words
# notr^ -> notR
# ar-bR^ => aRbR
b=gensub(/-([^-]+)\^$/,"\\1",1,a) ;
if (b!=a) { # there is a schwa to delete
a=b;
$phons=substr($phons,1,length($phons)-1);
n-;
}
# meme chose quand schwa=’*’
b=gensub(/-([^-]+)\*$/,"\\1",1,a) ;
if (b!=a) { # there is a schwa to delete
a=b;
$phons=substr($phons,1,length($phons)-1);
n-;
}
102
103
# compute the CVY skeleton
sk= " ";
for (i=1;i<=length(a);i++) {
ph=substr(a,i,1);
if (ph~V) sk=sk"V";
else if ((ph~C)||(ph~L)) sk=sk"C";
else if (ph~Y) sk=sk"Y";
else sk=sk ph;
}
}
114
{ print $0,a,n,sk }