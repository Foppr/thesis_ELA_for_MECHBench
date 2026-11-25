import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.coupling_strengths = np.random.uniform(0.5, 2.0, dim)
        self.curvature_factors = np.random.uniform(0.3, 1.5, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.ridge_parameters = np.random.uniform(0.15, 0.8, dim)
        # Additional parameters for improved conditioning and asymmetry
        self.asymmetry_factors = np.random.uniform(0.1, 0.5, dim)
        self.multiplier_factors = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic gradient components with hyperbolic tangent modulation and asymmetry
        for i in range(self.dim):
            xi = x[i]
            coupling = self.coupling_strengths[i]
            curvature = self.curvature_factors[i]
            freq = self.modulation_frequencies[i]
            phase = self.phase_shifts[i]
            ridge_param = self.ridge_parameters[i]
            asymmetry = self.asymmetry_factors[i]
            multiplier = self.multiplier_factors[i]
            
            # Enhanced hyperbolic tangent based chaotic gradient with ridge modulation and asymmetry
            tan_component = np.tanh(coupling * xi)
            ridge_term = ridge_param * np.sin(3.0 * xi) * np.cos(xi)
            asymmetric_term = asymmetry * np.exp(-0.5 * (xi - 1.0)**2) * np.sin(2.0 * xi)
            result += (curvature * xi**2 + 0.5 * tan_component * np.sin(freq * xi + phase) + ridge_term + asymmetric_term) * multiplier
            
        # Add cross-dimensional coupling with enhanced saddle-point dominance and multi-modal interference
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                # Enhanced saddle-point interaction with harmonic interference and multi-modal structure
                saddle_interaction = coupling * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.3 * np.tanh(xi * xj))
                harmonic_interference = 0.1 * np.sin(2.0 * xi) * np.cos(2.0 * xj)
                # Add multi-modal term for increased complexity
                multimodal_term = 0.05 * np.sin(4.0 * xi) * np.cos(3.0 * xj) * np.exp(-0.1 * (xi**2 + xj**2))
                result += saddle_interaction + harmonic_interference + multimodal_term
                
        # Add refined oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = 1.2 + 0.3 * np.sin(0.4 * i)
            freq = 1.5 + 0.6 * np.cos(0.5 * i)
            # Refined harmonic components with exponential decay and additional modulation
            result += amp * np.exp(-0.08 * xi**2) * np.sin(freq * xi) * (1.0 + 0.15 * np.cos(xi) + 0.05 * np.sin(2.0 * xi)) * (1.0 + 0.1 * np.sin(0.3 * xi))
            
        # Add global scaling and asymmetry with improved bias reduction
        global_scale = 1.0 + 0.15 * np.sin(0.4 * self.dim)
        result *= global_scale
        
        # Add final chaotic modulation with enhanced interference patterns
        chaotic_mod = 0.015 * np.sum(np.exp(-np.abs(x)) * np.sin(8.0 * x) * np.cos(3.0 * x))
        result += chaotic_mod
        
        # Add additional ridge structure for improved benchmark difficulty with asymmetric penalty
        ridge_penalty = 0.02 * np.sum((np.sin(2.0 * x)**2 + np.cos(2.0 * x)**2) * (1.0 + 0.2 * np.sin(x)))
        result += ridge_penalty
        
        # Add a multi-modal global structure to increase optimization challenge
        multimodal_global = 0.3 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x) * np.exp(-0.05 * x**2))
        result += multimodal_global
        
        return result