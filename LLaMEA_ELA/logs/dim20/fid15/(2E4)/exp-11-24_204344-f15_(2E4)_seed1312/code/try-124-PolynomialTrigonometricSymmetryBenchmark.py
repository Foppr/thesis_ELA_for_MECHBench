import numpy as np

class PolynomialTrigonometricSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial polynomial component with chaotic scaling
        r = np.sqrt(np.sum(x**2))
        radial = (r**4 + 0.5*r**3 - 2*r**2 + 1.5*r + 0.1) * np.exp(-0.1 * r)
        
        # Trigonometric coupling with dynamic phase shifts
        trig_coupling = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.7) * np.cos(i * 0.3)
            freq = 2.0 + 0.5 * np.sin(i * 0.9)
            trig_coupling += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 1.2)
        
        # Polynomial chaos with fractional exponents and random coefficients
        poly_chaos = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.8)
            exp = 1.5 + 0.4 * np.sin(i * 0.6)
            poly_chaos += coeff * (x[i]**exp + 0.5 * x[i]**(exp*0.7) - 0.3 * x[i])
        
        # Cross-dimensional coupling with variable interaction strength
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.3 * np.sin(i * j * 0.4) + 0.2 * np.cos(i * j * 0.6)
                coupling = strength * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                cross_coupling += coupling
        
        # Symmetric potential wells with variable depth and width
        wells = 0.0
        for i in range(self.dim):
            well_depth = 2.0 + 0.8 * np.sin(i * 0.5)
            well_width = 0.8 + 0.4 * np.cos(i * 0.7)
            wells += well_depth * (x[i]**2 - 2*x[i] + 1)**well_width
        
        # Oscillatory component with frequency modulation
        oscillatory = 0.0
        for i in range(self.dim):
            freq_mod = 3.0 + 2.0 * np.sin(i * 0.3)
            oscillatory += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) * np.exp(-0.5 * x[i]**2)
        
        # Final weighted combination
        return 0.6 * radial + 0.7 * trig_coupling + 0.8 * poly_chaos + 0.9 * cross_coupling + \
               1.0 * wells + 1.1 * oscillatory