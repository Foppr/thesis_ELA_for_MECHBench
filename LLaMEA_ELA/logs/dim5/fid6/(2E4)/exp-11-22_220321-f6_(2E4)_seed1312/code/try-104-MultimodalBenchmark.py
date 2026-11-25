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
        
        # Polynomial term with varying exponents
        poly_term = 0.0
        for i in range(self.dim):
            exp = self.poly_degree + int(i * 0.5) % 3
            poly_term += (x[i] ** exp) * (1 + 0.2 * np.sin(i))
            
        # Trigonometric oscillations with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.trig_freq + 0.5 * np.cos(i)
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial basis functions with adaptive widths
        rbf_term = 0.0
        for i in range(self.dim):
            width = self.rbf_width + 0.3 * np.sin(i)
            rbf_term += np.exp(-0.5 * (x[i] / width) ** 2)
            
        # Cross-dimensional asymmetric interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_factor = 1 + self.asymmetry_factor * np.sin(i - j)
                cross_term += asym_factor * np.exp(-0.2 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                
        # Adaptive conditioning based on dimension
        cond_term = 0.0
        for i in range(self.dim):
            condition = 10.0 + 5.0 * np.sin(i * 0.3)
            cond_term += condition * x[i]**2
            
        # Global phase shift and scaling
        phase_shift = np.sum(x) * 0.1
        global_scale = 1.0 + 0.1 * np.sin(phase_shift)
        
        return global_scale * (0.3 * poly_term + 0.4 * trig_term + 0.2 * rbf_term + 0.5 * cross_term + 0.3 * cond_term)