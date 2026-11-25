import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.coupling_strengths = np.random.uniform(0.4, 2.0, dim)
        self.curvature_factors = np.random.uniform(0.15, 1.4, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.ridge_parameters = np.random.uniform(0.15, 0.8, dim)
        
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
            ridge_param = self.ridge_parameters[i]
            
            # Enhanced hyperbolic tangent based chaotic gradient with ridge modulation
            tan_component = np.tanh(coupling * xi)
            ridge_term = ridge_param * np.sin(2.5 * xi) * np.cos(1.5 * xi)
            result += (curvature * xi**2 + 0.5 * tan_component * np.sin(freq * xi + phase) + ridge_term) * (1.0 + 0.25 * np.cos(xi))
            
        # Add cross-dimensional coupling with enhanced saddle-point dominance
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                # Enhanced saddle-point interaction with harmonic interference
                saddle_interaction = coupling * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.35 * np.tanh(xi * xj))
                harmonic_interference = 0.12 * np.sin(2.5 * xi) * np.cos(2.5 * xj)
                result += saddle_interaction + harmonic_interference
                
        # Add refined oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = 1.3 + 0.2 * np.sin(0.5 * i)
            freq = 1.7 + 0.5 * np.cos(0.6 * i)
            # Refined harmonic components with exponential decay
            result += amp * np.exp(-0.09 * xi**2) * np.sin(freq * xi) * (1.0 + 0.18 * np.cos(xi) + 0.07 * np.sin(2.0 * xi))
            
        # Add global scaling and asymmetry with improved bias reduction
        global_scale = 1.0 + 0.18 * np.sin(0.45 * self.dim)
        result *= global_scale
        
        # Add final chaotic modulation with enhanced interference patterns
        chaotic_mod = 0.02 * np.sum(np.exp(-np.abs(x)) * np.sin(8.5 * x) * np.cos(3.5 * x))
        result += chaotic_mod
        
        # Add additional ridge structure for improved benchmark difficulty
        ridge_penalty = 0.025 * np.sum(np.sin(2.5 * x)**2 + np.cos(2.5 * x)**2)
        result += ridge_penalty
        
        return result