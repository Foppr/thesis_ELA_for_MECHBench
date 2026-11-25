import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with dynamic scaling
        f_val = 0.5 * np.sum(x**4) + 0.3 * np.sum(x**2) * (1.0 + 0.2 * np.sin(0.5 * np.sum(x**2)))
        
        # Radial basis function components with varying widths and centers
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                center = np.array([2.0, -1.5, 1.0])
                sigma = np.array([0.8, 1.2, 0.6])
                diff = x[i:i+3] - center
                f_val += 0.4 * np.exp(-0.5 * np.sum((diff/sigma)**2))
                
        # Dynamic coupling terms with time-like chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += (x[i] - x[j])**4 * np.sin(0.3 * (x[i] + x[j])) * np.exp(-0.1 * abs(x[i] - x[j]))
        f_val += 0.25 * coupling_term
        
        # Polynomial chaos expansion with multiple interaction terms
        poly_expansion = 0.0
        for i in range(self.dim):
            poly_expansion += (x[i]**3) * np.cos(0.4 * x[i]) + (x[i]**2) * np.sin(0.6 * x[i])
        f_val += 0.3 * poly_expansion
        
        # Saddle point structure with enhanced directional dependency
        saddle_term = 0.0
        for i in range(self.dim - 1):
            saddle_term += (x[i]**2 - x[i+1]**2) * np.sin(0.5 * (x[i] + x[i+1]))
        f_val += 0.2 * saddle_term
        
        # Additional multimodal components with varying frequencies
        freq_multimodal = 0.0
        for i in range(self.dim):
            freq_multimodal += 0.3 * np.sin(18 * x[i]) * np.cos(12 * x[i]) * (1.0 + 0.15 * np.sin(3 * x[i]))
        f_val += 0.2 * freq_multimodal
        
        # Cross-dimensional polynomial interactions
        cross_poly = 0.0
        for i in range(self.dim - 2):
            cross_poly += x[i] * x[i+1] * x[i+2] * np.cos(0.3 * (x[i] + x[i+1] + x[i+2]))
        f_val += 0.15 * cross_poly
        
        # Chaotic modulation with improved distribution of local optima
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += 0.2 * np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.exp(-0.15 * abs(x[i]))
        f_val += 0.15 * chaotic_mod
        
        # Asymmetric Gaussian peaks with dynamic scaling
        asym_gauss = 0.0
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                asym_gauss += 0.25 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[i+1] + 2.0)**2 + 
                                                   (x[i+2] - 1.0)**2 + (x[i+3] + 1.5)**2))
        f_val += asym_gauss
        
        return f_val