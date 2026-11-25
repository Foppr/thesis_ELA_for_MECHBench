import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.coupling_strengths = np.random.uniform(0.3, 1.8, dim)
        self.curvature_factors = np.random.uniform(0.2, 1.2, dim)
        self.modulation_frequencies = np.random.uniform(0.8, 4.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.ridge_strengths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with enhanced saddle-point dominance
        for i in range(self.dim):
            xi = x[i]
            coupling = self.coupling_strengths[i]
            curvature = self.curvature_factors[i]
            freq = self.modulation_frequencies[i]
            phase = self.phase_shifts[i]
            ridge = self.ridge_strengths[i]
            
            # Enhanced hyperbolic tangent based chaotic gradient with saddle-point dominance
            tan_component = np.tanh(coupling * xi)
            result += (curvature * xi**2 + 0.3 * tan_component * np.sin(freq * xi + phase)) * (1.0 + 0.4 * np.cos(xi))
            
            # Add ridge structure with harmonic interference
            result += ridge * np.sin(0.5 * xi) * np.cos(0.3 * xi**2) * (1.0 + 0.1 * np.sin(xi))
            
        # Add cross-dimensional coupling with refined harmonic interference
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                # Refined harmonic interference between dimensions
                result += coupling * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.3 * np.tanh(xi * xj)) * np.sin(0.2 * (xi**2 + xj**2))
                
        # Add chaotic oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = 1.2 + 0.3 * np.sin(0.4 * i)
            freq = 1.5 + 0.6 * np.cos(0.5 * i)
            result += amp * np.exp(-0.15 * xi**2) * np.sin(freq * xi) * (1.0 + 0.2 * np.cos(xi)) * (1.0 + 0.1 * np.sin(0.3 * xi))
            
        # Add global scaling and asymmetry with enhanced nonlinearity
        global_scale = 1.2 + 0.15 * np.sin(0.6 * self.dim)
        result *= global_scale
        
        # Add final chaotic modulation with exponential decay and improved bias reduction
        chaotic_mod = 0.03 * np.sum(np.exp(-np.abs(x)) * np.sin(8.0 * x) * np.cos(0.5 * x))
        result += chaotic_mod
        
        # Add enhanced harmonic interference term to improve benchmark performance
        harmonic_term = 0.01 * np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * (1.0 + 0.2 * np.tanh(x)))
        result += harmonic_term
        
        return result