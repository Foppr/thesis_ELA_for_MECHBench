import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural network parameters
        self.weights = np.random.randn(dim, dim) * 0.5
        self.biases = np.random.randn(dim) * 0.3
        self.temporal_decay = 0.95
        self.activation_scale = 2.0
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Initialize neural state
        state = x_scaled.copy()
        
        # Simulate chaotic neural dynamics over multiple time steps
        total_energy = 0.0
        for t in range(20):
            # Apply recurrent connections with dynamic weights
            weighted_input = np.dot(self.weights, state)
            
            # Dynamic activation function with time-varying parameters
            dynamic_activation = np.tanh(weighted_input + self.biases)
            
            # Add temporal dynamics and chaotic behavior
            state = self.temporal_decay * state + (1.0 - self.temporal_decay) * dynamic_activation
            
            # Apply non-stationary scaling factors
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * t)
            total_energy += np.sum(state**2) * scale_factor
            
        # Multi-scale fitness landscape with harmonic interactions
        harmonic_fitness = 0.0
        for i in range(self.dim):
            # Multiple harmonic components with varying frequencies and amplitudes
            freq1 = 2.0 + 0.5 * np.sin(i * 0.7)
            freq2 = 3.0 + 0.3 * np.cos(i * 0.5)
            amp1 = 1.5 + 0.2 * np.sin(i * 0.9)
            amp2 = 1.2 + 0.4 * np.cos(i * 0.6)
            
            harmonic_fitness += amp1 * np.sin(freq1 * state[i]) + amp2 * np.cos(freq2 * state[i])
        
        # Cross-dimensional interaction terms with varying coupling strengths
        interaction_fitness = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.8 + 0.2 * np.sin(0.5 * (i + j))
                interaction_fitness += coupling * np.sin(state[i] + state[j]) * np.cos(state[i] - state[j])
        
        # Add chaotic basin structure with varying depth and width
        basin_fitness = 0.0
        for i in range(self.dim):
            # Create multi-modal basins with different characteristic widths
            basin_width = 0.3 + 0.2 * np.sin(i * 0.4)
            basin_depth = 1.0 + 0.5 * np.cos(i * 0.6)
            basin_center = 0.2 * np.sin(i * 0.8)
            
            distance = np.abs(state[i] - basin_center)
            basin_fitness += basin_depth * np.exp(-distance**2 / (2 * basin_width**2))
        
        # Combine all components with dynamic weighting
        return 0.7 * total_energy + 0.5 * harmonic_fitness + 0.6 * interaction_fitness + 0.4 * basin_fitness