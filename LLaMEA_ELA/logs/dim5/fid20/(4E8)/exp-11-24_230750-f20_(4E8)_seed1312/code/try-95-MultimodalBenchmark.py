import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic interactions with fractional exponents and multi-scale coupling
        frac_exp = np.sum(np.abs(x)**1.7 * np.exp(-0.3 * np.abs(x)) * np.sin(3.2 * x))
        
        # Novel fractional polynomial cross-terms with non-integer powers and alternating signs
        poly_cross = 0.4 * np.sum(x[:-3]**2.3 * x[1:-2]**1.8 * x[2:-1]**3.1 * x[3:]**2.7 - 
                                x[:-3]**1.9 * x[1:-2]**2.5 * x[2:-1]**1.6 * x[3:]**3.3)
        
        # Enhanced Gaussian ridge coupling with dynamic widths and multi-dimensional interaction
        ridge_sum = 0.0
        for i in range(min(5, self.dim)):
            center = np.cos(i * np.pi / 4) * 4.0
            width = 1.0 + 0.5 * np.sin(i * np.pi / 2)
            ridge_sum += np.exp(-0.3 * ((x[i] - center) / width)**2.5)
        
        # Modified trigonometric wave interactions with fractional harmonics and dynamic phase shifts
        trig_waves = np.sum(np.sin(1.8 * np.pi * x**1.3) * np.cos(3.7 * np.pi * x**1.4) * 
                           np.exp(-0.25 * np.abs(x)) * np.sin(0.9 * np.pi * x**1.2))
        
        # Novel hyperbolic tangent coupling with fractional orders and adaptive weights
        tanh_coupling = 0.7 * np.sum(np.tanh(0.8 * x[:-3] + 1.2 * x[1:-2] + 0.9 * x[2:-1] + 1.1 * x[3:]) * 
                                   np.tanh(2.2 * x[:-3] - 0.7 * x[1:-2] + 1.5 * x[2:-1] - 0.6 * x[3:]))
        
        # Enhanced radial basis functions with fractional centers and variable widths
        rbf_sum = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / 5) * 2.5
            width = 1.3 + 0.3 * np.cos(i * np.pi / 4)
            rbf_sum += np.exp(-0.4 * ((x[i] - center) / width)**1.8)
        
        # Dynamic conditioning with fractional scaling and multi-scale curvature factors
        condition_factor = 1.0 + 0.6 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)**1.5) + \
                          0.4 * np.cos(self.dim * 0.25) * np.std(x**1.3) + \
                          0.2 * np.sin(self.dim * 0.5) * np.max(np.abs(x)**1.7)
        
        # Quadratic basin with fractional powers, dynamic scaling, and enhanced coupling terms
        quadratic = condition_factor * np.sum((x**2.2) * (1.0 + 0.4 * x**3.1))
        
        # Additional chaotic noise component with fractional frequency modulation
        noise = 0.08 * np.random.rand() * np.sum(np.sin(5.5 * x**1.2) * np.cos(2.8 * x**1.3))
        
        # Combined function value with additional interaction terms and improved fitness landscape
        return quadratic + frac_exp + poly_cross + ridge_sum + trig_waves + tanh_coupling + rbf_sum + noise