import numpy as np

class ChaoticRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic components
        chaotic_sum = 0.0
        r = 3.95  # Chaotic parameter
        for i in range(self.dim):
            logistic_val = r * x[i] * (1 - x[i])
            chaotic_sum += 0.5 * logistic_val**2
        
        # Radial basis functions with dynamic centers
        rbf_sum = 0.0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            center = centers[i] + 0.1 * np.sin(2 * np.pi * x[i])
            width = 0.5 + 0.3 * np.cos(x[i])
            rbf_sum += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Multi-scale sine-cosine interference patterns
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1 + 0.5 * np.sin(x[i])
                freq_j = 1 + 0.5 * np.cos(x[j])
                coupling = 1.2 * np.exp(-0.2 * (x[i] - x[j])**2)
                interference_sum += coupling * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Polynomial chaos with chaotic modulation
        poly_chaos = 0.0
        for i in range(self.dim):
            modulator = 1 + 0.3 * np.sin(5 * x[i])
            poly_chaos += (x[i]**4 - 2*x[i]**2 + 1) * modulator
        
        # Boundary penalty with multi-modal components
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_penalty += 1.5 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.4 * np.sin(8 * x[i]))
            else:
                boundary_penalty += 1.8 * np.exp(-0.4 * (x[i] - 5.0)**2) * (1 + 0.3 * np.cos(6 * x[i]))
        
        # Fractal-like harmonic coupling
        fractal_harmonic = 0.0
        for i in range(self.dim):
            fractal_harmonic += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i])
        
        # Time-varying radial basis functions with chaotic centers
        time_rbf = 0.0
        for i in range(self.dim):
            center = x[i] + 0.2 * np.sin(3 * x[i])
            width = 0.8 + 0.2 * np.cos(x[i])
            time_rbf += 1.5 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Multi-scale chaotic coupling
        multi_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_factor = np.sin(3 * x[i]) * np.cos(4 * x[j])
                multi_chaos += chaos_factor * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric penalty near boundaries
        asym_penalty = 0.0
        for i in range(self.dim):
            asym_penalty += 0.8 * np.exp(-0.5 * (x[i] + 5.0)**2) * np.sin(12 * x[i]) + \
                           1.0 * np.exp(-0.5 * (x[i] - 5.0)**2) * np.cos(10 * x[i])
        
        # Final combined function
        result = chaotic_sum + rbf_sum + interference_sum + poly_chaos + boundary_penalty + \
                 fractal_harmonic + time_rbf + multi_chaos + asym_penalty
        
        return result