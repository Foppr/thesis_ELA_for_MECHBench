import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for hyperelliptic basins
        self.basin_params = [np.random.uniform(1.5, 4.0) for _ in range(dim)]
        self.saddle_strength = [np.random.uniform(2.0, 5.0) for _ in range(dim)]
        self.time_phase = np.random.rand() * 2 * np.pi
        # Quantum-like interaction parameters
        self.quantum_freq = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.resonance_amp = np.random.uniform(0.1, 0.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperelliptic basin component
        basins = 0
        for i in range(self.dim):
            param = self.basin_params[i]
            # Hyperellipse function: |x|^p + |y|^p = 1 with higher powers
            basins += (np.abs(x[i]) ** param) / param
            
        # Quantum-like saddle points with interference patterns
        saddles = 0
        for i in range(self.dim):
            strength = self.saddle_strength[i]
            # Quantum interference term
            quantum_term = np.sin(self.quantum_freq[i] * x[i] + self.time_phase)
            # Combined quantum-saddle interaction
            saddle_term = strength * (x[i]**2 - 1) * quantum_term
            saddles += saddle_term
            
        # Adaptive gradient field with stochastic resonance
        gradients = 0
        for i in range(self.dim):
            # Adaptive scaling based on local fitness landscape
            adaptive_scale = 1.0 + 0.3 * np.sin(x[i] * self.time_phase)
            grad_term = adaptive_scale * np.cos(x[i] * np.pi / 2.0) + \
                       self.resonance_amp * np.sin(self.time_phase * x[i])
            gradients += grad_term
            
        # Cross-dimension coupling with stochastic weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stochastic coupling weight with memory effect
                time_weight = 0.3 + 0.7 * np.cos(self.time_phase + x[i] + x[j])
                coupling += time_weight * np.exp(-np.abs(x[i] - x[j])) * (i + j + 1)
                
        # Stochastic noise with frequency modulation
        noise_amp = 0.2 * (1.0 + 0.3 * np.cos(self.time_phase))
        noise = noise_amp * np.random.normal(0, 1, size=self.dim).sum()
        
        # Add fractal-like self-similarity component
        fractal = 0
        for i in range(self.dim):
            fractal += np.sin(x[i] * 2**i) * (1.0 / (2**i))
            
        # Combine all components with dynamic weights
        result = 1.5 * basins + 1.0 * saddles + 0.7 * gradients + 0.5 * coupling + 0.2 * noise + 0.3 * fractal
        
        # Add dimensionality scaling with exponential factor
        dim_factor = np.exp(self.dim / 10.0) / np.exp(1.0)
        result *= (1.0 + 0.4 * dim_factor)
        
        return result