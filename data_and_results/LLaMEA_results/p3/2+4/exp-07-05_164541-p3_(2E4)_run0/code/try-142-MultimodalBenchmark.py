import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying exponents and random coefficients
        poly_chaos = np.sum((x**2 + 0.5*x**3 - 0.3*x**5 + 0.1*x**7) * np.sin(2 * np.pi * x))
        
        # Radial basis function with Gaussian kernels and varying widths
        rbfs = 0.0
        for i in range(10):
            center = np.random.uniform(-5, 5, self.dim)
            width = np.random.uniform(0.5, 2.0)
            rbfs += np.exp(-width * np.sum((x - center)**2))
        
        # Temporal coupling with delayed feedback and dynamic weights
        temporal_coupling = 0.0
        for i in range(self.dim - 1):
            temporal_coupling += (x[i] - x[i+1])**4 * np.sin(10 * np.pi * x[i]) * np.cos(8 * np.pi * x[i+1])
        
        # Sine-wave modulation with multiple frequencies and amplitudes
        wave_mod = np.sum(np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) * 
                         np.sin(9 * np.pi * x) * np.cos(6 * np.pi * x) * 
                         np.sin(3 * np.pi * x))
        
        # Multi-scale interaction terms with varying coupling strengths
        multi_scale = np.sum((x[:-1] * x[1:])**(1.5) * np.sin(25 * np.pi * x[:-1]) * 
                            np.cos(20 * np.pi * x[1:]) + 
                            (x[:-2] + x[2:])**(2.5) * np.sin(15 * np.pi * x[:-2]) * 
                            np.cos(10 * np.pi * x[2:]))
        
        # Add a global offset and normalize
        return 0.7 * poly_chaos + 0.3 * rbfs + 0.2 * temporal_coupling + 0.15 * wave_mod + 0.25 * multi_scale + 3.0