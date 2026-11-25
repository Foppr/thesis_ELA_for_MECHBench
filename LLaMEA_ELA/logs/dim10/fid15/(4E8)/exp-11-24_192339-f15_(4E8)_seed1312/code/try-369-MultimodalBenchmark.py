import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural network parameters
        self.weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.biases = np.random.uniform(-0.5, 0.5, dim)
        self.time_phase = np.random.uniform(0, 2*np.pi, dim)
        self.resonance_freq = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Dynamic neural network layer with time-varying weights
        dynamic_layer = 0
        for i in range(self.dim):
            # Time-varying weight modulation based on input and phase
            modulated_weight = self.weights[i, i] * (1 + 0.3 * np.sin(x[i] + self.time_phase[i]))
            # Nonlinear activation with dynamic parameters
            activation = np.tanh(modulated_weight * x[i] + self.biases[i])
            dynamic_layer += activation**2
        
        # Chaotic resonance component with multi-scale frequency modulation
        resonance_component = 0
        for i in range(self.dim):
            freq_mod = self.resonance_freq[i] * (1 + 0.4 * np.cos(0.3 * x[i] + self.time_phase[i]))
            resonance_component += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with adaptive strength
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.8 + 0.2 * np.sin(0.5 * (x[i] + x[j]) + self.time_phase[i])
                coupling_component += coupling_strength * np.sin(x[i] - x[j])**2
        
        # Multi-scale fractal interference with dynamic scaling
        fractal_component = 0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.5 * np.sin(0.4 * x[i] + self.time_phase[i])
            fractal_component += np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i]**3) * np.exp(-0.2 * x[i]**2)
        
        # Adaptive ridge with variable curvature and dynamic offset
        ridge_component = 0
        for i in range(self.dim):
            curvature = 1.2 + 0.3 * np.cos(0.6 * x[i] + self.time_phase[i])
            offset = 0.5 * np.sin(0.8 * x[i] + self.time_phase[i])
            ridge_component += curvature * (x[i]**4 - 2 * x[i]**2 + offset) * np.exp(-0.15 * x[i]**2)
        
        # Final combined landscape
        return (0.3 * dynamic_layer + 0.25 * resonance_component + 
                0.2 * coupling_component + 0.15 * fractal_component + 
                0.1 * ridge_component)