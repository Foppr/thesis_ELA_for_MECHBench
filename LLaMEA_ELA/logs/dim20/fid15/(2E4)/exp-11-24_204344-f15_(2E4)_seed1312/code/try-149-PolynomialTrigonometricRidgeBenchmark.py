import numpy as np

class PolynomialTrigonometricRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos component with fractional exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**3.5 + 0.5 * x[i]**2.8 + 0.1 * x[i]**1.7) * np.exp(-0.1 * np.abs(x[i]))
        
        # Trigonometric coupling with adaptive frequencies and amplitudes
        trig_coupling = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            trig_coupling += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.5 * i)
        
        # Adaptive ridge structure with varying widths and heights
        ridges = 0.0
        for i in range(self.dim):
            ridge_width = 0.5 + 0.3 * np.sin(0.4 * i)
            ridge_height = 1.2 + 0.8 * np.cos(0.6 * i)
            ridges += ridge_height * np.exp(-0.5 * ((x[i] - 0.5 * i) / ridge_width)**2)
        
        # Cross-dimensional interaction with fractional coupling strengths
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 + 0.2 * np.sin(0.3 * (i + j))
                cross_interaction += coupling_strength * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Multi-scale harmonic modulation with dynamic phase shifts
        harmonic_mod = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.2 * np.sin(0.7 * i)
            freq = 3.0 + 2.0 * np.cos(0.5 * i)
            phase_shift = 0.5 * np.sin(0.8 * i)
            harmonic_mod += scale * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i])
        
        # Asymmetric potential wells with varying depths and positions
        wells = 0.0
        for i in range(self.dim):
            well_pos = -1.0 + 2.0 * np.sin(0.6 * i)
            well_depth = 1.5 + 0.5 * np.cos(0.4 * i)
            wells += well_depth * (x[i] - well_pos)**2 * np.exp(-0.3 * (x[i] - well_pos)**2)
        
        # Fractional power scaling with irregular exponents
        fractional_power = 0.0
        for i in range(self.dim):
            exponent = 1.2 + 0.8 * np.sin(0.9 * i)
            fractional_power += np.abs(x[i])**exponent
        
        # Final landscape combining all components with adaptive weights
        return 0.4 * poly_chaos + 0.6 * trig_coupling + 0.5 * ridges + 0.7 * cross_interaction + \
               0.8 * harmonic_mod + 0.9 * wells + 1.0 * fractional_power