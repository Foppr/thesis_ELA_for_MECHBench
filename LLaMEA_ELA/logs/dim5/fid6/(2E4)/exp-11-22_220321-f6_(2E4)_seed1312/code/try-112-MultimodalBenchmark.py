import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.trig_freq = 2.0
        self.rbf_width = 1.5
        self.asymmetry_factor = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial term with varying exponents and adaptive coefficients
        poly_term = 0.0
        for i in range(self.dim):
            exp = self.poly_degree + int(i * 0.5) % 3
            coeff = 1.0 + 0.3 * np.sin(i * 0.7)
            poly_term += coeff * (x[i] ** exp)
            
        # Trigonometric oscillations with chaotic frequency modulation and phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.trig_freq + 0.4 * np.sin(i * 0.5 + np.cos(i * 0.3))
            phase = 0.2 * np.cos(i * 0.3 + np.sin(i * 0.4))
            trig_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Radial basis functions with dynamic widths and adaptive centers
        rbf_term = 0.0
        for i in range(self.dim):
            width = self.rbf_width + 0.2 * np.sin(i * 0.6)
            center = 1.0 + 0.5 * np.cos(i * 0.4)
            rbf_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            
        # Cross-dimensional asymmetric interactions with chaotic coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin(i * 0.4 + j * 0.3 + np.cos(i * 0.2 + j * 0.1))
                asym_factor = 1 + self.asymmetry_factor * np.sin(i - j + np.cos(i * 0.3))
                cross_term += coupling * asym_factor * np.exp(-0.3 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = 0.0
        for i in range(self.dim):
            condition = 15.0 + 10.0 * np.sin(i * 0.4)
            cond_term += condition * x[i]**2
            
        # Global phase shift and scaling with dynamic adjustment
        phase_shift = np.sum(x) * 0.15
        global_scale = 1.0 + 0.2 * np.sin(phase_shift + np.cos(phase_shift * 0.5))
        
        # Additional chaotic harmonic component for increased complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(3.0 * x[i] + np.cos(x[i] * 0.7)) * np.cos(2.0 * x[i] + np.sin(x[i] * 0.5))
            
        return global_scale * (0.25 * poly_term + 0.35 * trig_term + 0.15 * rbf_term + 0.4 * cross_term + 0.2 * cond_term + 0.1 * harmonic_term)