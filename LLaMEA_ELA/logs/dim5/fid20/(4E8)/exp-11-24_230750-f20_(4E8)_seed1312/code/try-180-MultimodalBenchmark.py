import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Slight modification to chaotic sine-cosine wave interactions with altered frequencies and coupling
        sc_waves = np.sum(np.sin(2.9 * np.pi * x) * np.cos(4.8 * np.pi * x) * 
                         np.exp(-0.35 * np.abs(x)) * np.sin(1.9 * np.pi * x))
        
        # Modified adaptive radial basis functions with shifted centers and adjusted widths
        rbf_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / 2.1) * 3.8
            width = 1.3 + 0.3 * np.cos(i * np.pi / 2.9)
            rbf_sum += np.exp(-0.32 * ((x[i] - center) / width)**2)
        
        # Hyperbolic tangent coupling with modified weights and interaction pattern
        tanh_coupling = 0.8 * np.sum(np.tanh(x[:-3] + 0.4 * x[1:-2] + 0.9 * x[2:-1] + 0.2 * x[3:]) * 
                                   np.tanh(2.5 * x[:-3] - 0.8 * x[1:-2] + 0.7 * x[2:-1] - 0.5 * x[3:]))
        
        # Adjusted polynomial cross-terms with modified exponents and interaction scaling
        poly_cross = 0.38 * np.sum(x[:-3]**5 * x[1:-2]**4 * x[2:-1]**3 * x[3:]**5 - 
                                 x[:-3]**4 * x[1:-2]**5 * x[2:-1]**4 * x[3:]**4)
        
        # Dynamic conditioning with updated multi-scale factors and curvature
        condition_factor = 1.0 + 0.48 * np.sin(self.dim * 0.39) * np.mean(np.abs(x)) + \
                          0.32 * np.cos(self.dim * 0.25) * np.std(x) + \
                          0.18 * np.sin(self.dim * 0.58) * np.max(np.abs(x))
        
        # Quadratic basin with modified weights and enhanced scaling
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.32 * x**4))
        
        # Slight adjustment to chaotic noise component with modified intensity and frequency
        noise = 0.1 * np.random.rand() * np.sum(np.sin(6.9 * x) * np.cos(3.0 * x))
        
        # Modified exponential decay with altered interaction rates
        exp_decay = np.sum(np.exp(-0.55 * (x / (1.0 + 0.45 * np.abs(x)))**5))
        
        # Combined function value with updated interaction terms
        return quadratic + sc_waves + tanh_coupling + rbf_sum + poly_cross + exp_decay + noise