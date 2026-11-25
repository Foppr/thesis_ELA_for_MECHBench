import numpy as np

class ChaoticRBFInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic components with time-varying parameter
        chaotic_sum = 0.0
        r = 3.95 + 0.05 * np.sin(0.5 * np.sum(x))  # Adaptive chaos parameter
        for i in range(self.dim):
            logistic_val = r * x[i] * (1 - x[i])
            chaotic_sum += 0.5 * logistic_val**2
        
        # Radial basis functions with dynamic centers and adaptive widths
        rbf_sum = 0.0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            center = centers[i] + 0.1 * np.sin(2 * np.pi * x[i]) + 0.05 * np.cos(3 * x[i])
            width = 0.5 + 0.3 * np.cos(x[i]) + 0.1 * np.sin(2 * x[i])
            rbf_sum += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Multi-scale sine-cosine interference patterns with adaptive coupling
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1 + 0.5 * np.sin(x[i]) + 0.2 * np.cos(2 * x[i])
                freq_j = 1 + 0.5 * np.cos(x[j]) + 0.2 * np.sin(2 * x[j])
                coupling = 1.2 * np.exp(-0.2 * (x[i] - x[j])**2) * (1 + 0.3 * np.sin(x[i] + x[j]))
                interference_sum += coupling * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Polynomial chaos with chaotic modulation and adaptive exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            modulator = 1 + 0.3 * np.sin(5 * x[i]) + 0.1 * np.cos(7 * x[i])
            exponent = 4 + 0.5 * np.sin(x[i])
            poly_chaos += (x[i]**exponent - 2*x[i]**2 + 1) * modulator
        
        # Boundary penalty with multi-modal components and adaptive penalties
        boundary_penalty = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_penalty += 1.5 * np.exp(-0.3 * (x[i] + 5.0)**2) * (1 + 0.4 * np.sin(8 * x[i])) * (1 + 0.2 * np.cos(3 * x[i]))
            else:
                boundary_penalty += 1.8 * np.exp(-0.4 * (x[i] - 5.0)**2) * (1 + 0.3 * np.cos(6 * x[i])) * (1 + 0.2 * np.sin(4 * x[i]))
        
        # Fractal-like harmonic coupling with adaptive scaling
        fractal_harmonic = 0.0
        for i in range(self.dim):
            scale_factor = 1 + 0.3 * np.sin(0.5 * x[i])
            fractal_harmonic += scale_factor * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i])
        
        # Time-varying radial basis functions with chaotic centers and adaptive widths
        time_rbf = 0.0
        for i in range(self.dim):
            center = x[i] + 0.2 * np.sin(3 * x[i]) + 0.1 * np.cos(5 * x[i])
            width = 0.8 + 0.2 * np.cos(x[i]) + 0.1 * np.sin(3 * x[i])
            time_rbf += 1.5 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Multi-scale chaotic coupling with adaptive strength
        multi_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_factor = np.sin(3 * x[i]) * np.cos(4 * x[j]) * (1 + 0.2 * np.sin(x[i] + x[j]))
                strength = 0.8 + 0.2 * np.cos(x[i] - x[j])
                multi_chaos += strength * chaos_factor * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric penalty near boundaries with adaptive components
        asym_penalty = 0.0
        for i in range(self.dim):
            asym_penalty += 0.8 * np.exp(-0.5 * (x[i] + 5.0)**2) * np.sin(12 * x[i]) * (1 + 0.3 * np.cos(2 * x[i])) + \
                           1.0 * np.exp(-0.5 * (x[i] - 5.0)**2) * np.cos(10 * x[i]) * (1 + 0.3 * np.sin(3 * x[i]))
        
        # Novel fractal-like harmonic coupling with multi-scale modulation
        novel_fractal = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(x[i]) + 0.3 * np.cos(2 * x[i])
            novel_fractal += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.7) * np.sin(freq_mod * x[i] * 0.5)
        
        # Adaptive coupling between dimensions with chaotic modulation
        adaptive_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin(2 * x[i] + 3 * x[j])
                adaptive_coupling += coupling_strength * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Final combined function
        result = chaotic_sum + rbf_sum + interference_sum + poly_chaos + boundary_penalty + \
                 fractal_harmonic + time_rbf + multi_chaos + asym_penalty + novel_fractal + adaptive_coupling
        
        return result