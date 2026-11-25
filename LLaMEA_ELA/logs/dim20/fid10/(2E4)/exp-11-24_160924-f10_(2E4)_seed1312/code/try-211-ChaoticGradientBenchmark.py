import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with dimension-dependent randomness
        np.random.seed(42)
        self.coupling_strengths = np.random.uniform(0.3, 2.5, dim)
        self.curvature_factors = np.random.uniform(0.05, 2.0, dim)
        self.modulation_frequencies = np.random.uniform(0.5, 8.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.ridge_parameters = np.random.uniform(0.1, 1.0, dim)
        self.saddle_strengths = np.random.uniform(0.2, 1.5, dim)
        self.oscillation_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.interference_frequencies = np.random.uniform(1.5, 7.0, dim)
        self.harmonic_weights = np.random.uniform(0.1, 0.8, dim)
        self.cross_coupling_strengths = np.random.uniform(0.1, 1.2, (dim, dim))
        
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
            ridge_term = ridge_param * np.sin(3.0 * xi) * np.cos(xi)
            result += (curvature * xi**2 + 0.5 * tan_component * np.sin(freq * xi + phase) + ridge_term) * (1.0 + 0.3 * np.cos(xi))
            
        # Add cross-dimensional coupling with enhanced saddle-point dominance
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                saddle_strength = self.saddle_strengths[i] * self.saddle_strengths[j]
                cross_coupling = self.cross_coupling_strengths[i][j]
                
                # Enhanced saddle-point interaction with harmonic interference
                saddle_interaction = saddle_strength * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.4 * np.tanh(xi * xj))
                harmonic_interference = 0.2 * np.sin(self.interference_frequencies[i] * xi) * np.cos(self.interference_frequencies[j] * xj)
                
                # Add cross-dimensional interaction with exponential coupling
                cross_interaction = cross_coupling * np.exp(-0.5 * (xi - xj)**2) * np.sin(xi * xj)
                
                result += saddle_interaction + harmonic_interference + cross_interaction
                
        # Add refined oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            xi = x[i]
            amp = self.oscillation_amplitudes[i] + 0.3 * np.sin(0.5 * i)
            freq = self.interference_frequencies[i] + 0.6 * np.cos(0.6 * i)
            
            # Refined harmonic components with exponential decay and higher-order terms
            result += amp * np.exp(-0.15 * xi**2) * np.sin(freq * xi) * (1.0 + 0.3 * np.cos(xi) + 0.1 * np.sin(2.0 * xi) + 0.05 * np.cos(3.0 * xi))
            
        # Add global scaling and asymmetry with improved bias reduction
        global_scale = 1.0 + 0.3 * np.sin(0.6 * self.dim)
        result *= global_scale
        
        # Add final chaotic modulation with enhanced interference patterns
        chaotic_mod = 0.03 * np.sum(np.exp(-np.abs(x)) * np.sin(10.0 * x) * np.cos(5.0 * x))
        result += chaotic_mod
        
        # Add additional ridge structure for improved benchmark difficulty
        ridge_penalty = 0.05 * np.sum(np.sin(3.0 * x)**2 + np.cos(3.0 * x)**2)
        result += ridge_penalty
        
        # Add a new chaotic perturbation term with higher frequency components and nonlinear coupling
        perturbation = 0.015 * np.sum(np.sin(15.0 * x) * np.cos(8.0 * x) * np.tanh(x) * np.exp(-0.2 * x**2))
        result += perturbation
        
        # Add a complex interaction term with multiple harmonic frequencies
        multi_harmonic = 0.02 * np.sum(np.sin(4.0 * x) * np.cos(6.0 * x) * np.sin(2.0 * x) * np.cos(3.0 * x))
        result += multi_harmonic
        
        # Add a power-law scaling component to increase problem difficulty
        power_scaling = 0.01 * np.sum(np.abs(x)**3.5)
        result += power_scaling
        
        return result