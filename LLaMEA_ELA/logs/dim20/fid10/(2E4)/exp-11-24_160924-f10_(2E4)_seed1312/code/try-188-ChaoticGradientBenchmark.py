import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.coupling_strengths = np.random.uniform(0.5, 2.0, dim)
        self.curvature_factors = np.random.uniform(0.1, 1.5, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with hyperbolic tangent modulation
        for i in range(self.dim):
            xi = x[i]
            coupling = self.coupling_strengths[i]
            curvature = self.curvature_factors[i]
            freq = self.modulation_frequencies[i]
            phase = self.phase_shifts[i]
            
            # Hyperbolic tangent based chaotic gradient
            tan_component = np.tanh(coupling * xi)
            result += (curvature * xi**2 + 0.5 * tan_component * np.sin(freq * xi + phase)) * (1.0 + 0.3 * np.cos(xi))
            
        # Add cross-dimensional coupling with dynamic curvature
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                # Dynamic curvature interaction between dimensions
                result += coupling * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.2 * np.tanh(xi * xj))
                
        # Add chaotic oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = 1.0 + 0.5 * np.sin(0.3 * i)
            freq = 2.0 + 0.8 * np.cos(0.4 * i)
            result += amp * np.exp(-0.1 * xi**2) * np.sin(freq * xi) * (1.0 + 0.1 * np.cos(xi))
            
        # Add global scaling and asymmetry
        global_scale = 1.0 + 0.2 * np.sin(0.5 * self.dim)
        result *= global_scale
        
        # Add final chaotic modulation with exponential decay
        chaotic_mod = 0.02 * np.sum(np.exp(-np.abs(x)) * np.sin(10.0 * x))
        result += chaotic_mod
        
        return result