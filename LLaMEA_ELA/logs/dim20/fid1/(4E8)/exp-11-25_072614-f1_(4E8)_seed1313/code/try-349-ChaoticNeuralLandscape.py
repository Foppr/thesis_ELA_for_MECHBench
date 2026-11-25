import numpy as np

class ChaoticNeuralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic weight dynamics with fractal scaling
        self.weights = np.array([np.sin(0.7 * np.pi * i + 0.5 * np.sum(np.arange(dim))) for i in range(dim)])
        self.biases = np.array([np.cos(0.6 * np.pi * i + 0.4 * np.sum(np.arange(dim))) for i in range(dim)])
        # Multi-scale phase modulation with dynamic coupling
        self.phases = np.array([0.2 * np.sin(0.8 * np.pi * i + 0.6 * np.sum(np.arange(dim))) for i in range(dim)])
        # Fractal activation scales with chaotic variation
        self.scales = np.array([2.0 + 0.4 * np.cos(0.5 * np.pi * i + 0.4 * np.sum(np.arange(dim))) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced neural computation with fractal coupling
        neural_output = 0.0
        for i in range(self.dim):
            weighted_input = self.weights[i] * x[i] + self.biases[i]
            activation = np.tanh(weighted_input + self.phases[i])
            neural_output += activation * np.exp(-0.15 * x[i]**2)
        neural_output /= self.dim
        
        # Multi-scale fractal activation with enhanced chaotic coupling
        scale_activation = 0.0
        for i in range(self.dim):
            scaled_input = self.scales[i] * x[i]
            scale_activation += np.sin(scaled_input + 0.15 * np.sum(x)) * np.cos(scaled_input) * np.exp(-0.08 * x[i]**2)
        scale_activation /= self.dim
        
        # Dynamic phase modulation with fractal correlation
        phase_modulation = 0.0
        for i in range(self.dim):
            phase = self.phases[i] + 0.3 * np.sin(0.5 * np.pi * i + 0.2 * np.sum(x))
            phase_modulation += np.sin(x[i] + phase) * np.exp(-0.2 * x[i]**2)
        phase_modulation /= self.dim
        
        # Enhanced cross-dimensional coupling with fractal interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 + 0.5 * np.sin(0.6 * (i - j) + 0.3 * np.sum(x))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j] + 0.15 * np.sum(x)) * np.exp(-0.12 * (x[i]**2 + x[j]**2))
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal basin term with multi-scale chaotic variation
        basin_term = 0.0
        for i in range(self.dim):
            dim_scale = self.scales[i] + 0.3 * np.cos(0.7 * np.pi * i + 0.2 * np.sum(x))
            basin_term += (x[i]**4 - dim_scale * x[i]**3 + 0.7 * np.sin(np.sum(x))) * np.exp(-0.15 * x[i]**2)
        basin_term /= self.dim
        
        # Multi-modal interference with fractal frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 0.4 * np.sin(0.8 * np.pi * i + 0.4 * np.sum(x))
            interference += np.sin(freq_mod * x[i] + 0.2 * np.sum(x)) * np.cos(freq_mod * x[i]) * np.exp(-0.1 * x[i]**2)
        interference /= self.dim
        
        # Fractal weighting with chaotic normalization
        total_weights = np.abs(self.weights) / (np.sum(np.abs(self.weights)) + 1e-8)
        
        # Combine all terms with fractal weights and enhanced chaos
        result = (0.15 * total_weights[0] * neural_output + 
                 0.2 * total_weights[1] * scale_activation + 
                 0.15 * total_weights[2] * phase_modulation + 
                 0.25 * total_weights[3] * cross_coupling + 
                 0.15 * total_weights[4] * basin_term + 
                 0.1 * total_weights[5] * interference)
        
        return result