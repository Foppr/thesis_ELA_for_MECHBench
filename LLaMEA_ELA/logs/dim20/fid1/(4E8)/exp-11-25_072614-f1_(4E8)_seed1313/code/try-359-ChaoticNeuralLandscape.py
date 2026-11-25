import numpy as np

class ChaoticNeuralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic weight initialization with fractal scaling
        self.weights = np.array([np.sin(0.5 * np.pi * i + 0.3 * np.sum(np.arange(dim))) for i in range(dim)])
        self.biases = np.array([np.cos(0.4 * np.pi * i + 0.2 * np.sum(np.arange(dim))) for i in range(dim)])
        # Adaptive phase shifts with fractal modulation
        self.phases = np.array([0.1 * np.sin(0.6 * np.pi * i + 0.4 * np.sum(np.arange(dim))) for i in range(dim)])
        # Multi-scale activation parameters with fractal scaling
        self.scales = np.array([1.5 + 0.5 * np.cos(0.3 * np.pi * i + 0.2 * np.sum(np.arange(dim))) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced neural computation with fractal coupling
        neural_output = 0.0
        for i in range(self.dim):
            weighted_input = self.weights[i] * x[i] + self.biases[i]
            activation = np.tanh(weighted_input + self.phases[i])
            # Fractal scaling in activation
            fractal_scale = 1.0 + 0.2 * np.sin(0.5 * np.pi * i + 0.3 * np.sum(x))
            neural_output += activation * np.exp(-0.1 * x[i]**2) * fractal_scale
        neural_output /= self.dim
        
        # Multi-scale chaotic activation with fractal modulation
        scale_activation = 0.0
        for i in range(self.dim):
            scaled_input = self.scales[i] * x[i]
            # Fractal frequency modulation
            freq_mod = 1.2 + 0.3 * np.sin(0.4 * np.pi * i + 0.2 * np.sum(x))
            scale_activation += np.sin(freq_mod * scaled_input + 0.1 * np.sum(x)) * np.cos(scaled_input) * np.exp(-0.05 * x[i]**2)
        scale_activation /= self.dim
        
        # Adaptive phase modulation with fractal evolution
        phase_modulation = 0.0
        for i in range(self.dim):
            # Fractal phase adjustment
            phase = self.phases[i] + 0.15 * np.sin(0.3 * np.pi * i + 0.1 * np.sum(x))
            phase_modulation += np.sin(x[i] + phase) * np.exp(-0.15 * x[i]**2)
        phase_modulation /= self.dim
        
        # Fractal cross-dimensional coupling with modified strengths
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified coupling strength with stronger interaction
                coupling_strength = 1.2 + 0.35 * np.sin(0.4 * (i - j) + 0.2 * np.sum(x))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j] + 0.1 * np.sum(x)) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        cross_coupling /= (self.dim * (self.dim - 1) / 2.0)
        
        # Enhanced gradient-rich basin with fractal scaling and altered polynomial
        basin_term = 0.0
        for i in range(self.dim):
            # Fractal dimension scaling with modified coefficients
            dim_scale = self.scales[i] + 0.15 * np.cos(0.5 * np.pi * i + 0.1 * np.sum(x))
            basin_term += (x[i]**4 - dim_scale * x[i]**3 + 0.5 * np.sin(np.sum(x))) * np.exp(-0.1 * x[i]**2)
        basin_term /= self.dim
        
        # Fractal interference with chaotic frequency modulation
        interference = 0.0
        for i in range(self.dim):
            # Fractal frequency modulation with altered parameters
            freq_mod = 1.5 + 0.4 * np.sin(0.6 * np.pi * i + 0.3 * np.sum(x))
            interference += np.sin(freq_mod * x[i] + 0.15 * np.sum(x)) * np.cos(freq_mod * x[i]) * np.exp(-0.07 * x[i]**2)
        interference /= self.dim
        
        # Fractal dynamic weighting with improved balance
        total_weights = np.abs(self.weights) / (np.sum(np.abs(self.weights)) + 1e-8)
        
        # Combine all terms with fractal weights and improved basin connectivity
        result = (total_weights[0] * neural_output + 
                 total_weights[1] * scale_activation + 
                 total_weights[2] * phase_modulation + 
                 total_weights[3] * cross_coupling + 
                 total_weights[4] * basin_term + 
                 total_weights[5] * interference)
        
        # Add a modified polynomial term for better basin connectivity
        connectivity_term = 0.0
        for i in range(self.dim):
            connectivity_term += (x[i]**2 - 2.0 * x[i] + 1.0) * np.exp(-0.05 * x[i]**2)
        connectivity_term /= self.dim
        
        # Final result with improved basin connectivity and gradient structure
        result = result + 0.1 * connectivity_term
        
        return result