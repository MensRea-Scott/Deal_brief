#encoding: utf-8
__author__ = 'yyin'


class brief:
    Dealowner=u''
    Property=[]
    Licensee=u''
    Comdate=u''
    Enddate=u''
    Category=[]
    Channel=[]
    MG=0
    Payment={}
    Rytrate=0.0
    Selloff=u''

    def rate_to_txt(self.Rytrate):
        n=str(Rytrate*100)+'%'
        return unicode(n,'utf-8')

    def str_to_uni(txt):
        if type(txt)==str:
            return unicode(txt,'utf-8')
        else:
            return txt

    Template=ur"""Dear Guenther,

Per [Dealowner]'s request, attached is the Merchandise Licensing Agreement for [Property]. Below is the summary of
the agreement. Could you please kindly approve the attached at your earliest convenience? Thanks!


Parties: ODW (Ancillary WFOE) and [Licensee]

Licensed Property: [Property]

Licensed Period: from [Comdate] to [Enddate]

Licensed Articles: [Category]

Licensed channel: [Channel].

Advance/Minimum Guarantee: RMB[MG], among which:
(a)  RMB[Payment_amount] shall be paid [Payment_schedule];
(b)  RMB[Payment_amount] shall be paid by [Payment_schedule]

Royalty Rate: [Rytrate]

Sell-off period: [Selloff]
"""




