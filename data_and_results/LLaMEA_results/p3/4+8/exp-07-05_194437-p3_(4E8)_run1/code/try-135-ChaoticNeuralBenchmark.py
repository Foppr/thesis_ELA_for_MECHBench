import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic neural network parameters
        self.weights = np.random.randn(dim, dim) * 0.5
        self.biases = np.random.randn(dim) * 0.3
        self.delay_weights = np.random.randn(dim, dim) * 0.2
        self.time_delays = np.random.randint(1, 4, dim)
        self.coupling_strengths = np.random.rand(dim) * 2.0 + 1.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic neural network dynamics with time delays
        result = 0.0
        states = np.zeros(self.dim)
        
        for t in range(100):  # Simulate 100 time steps
            new_states = np.zeros(self.dim)
            for i in range(self.dim):
                # Compute input to neuron i
                input_val = self.biases[i]
                for j in range(self.dim):
                    # Standard connection
                    input_val += self.weights[i, j] * states[j]
                    # Delayed connection
                    delay_idx = (t - self.time_delays[i]) % 100
                    if delay_idx >= 0:
                        input_val += self.delay_weights[i, j] * states[j]
                
                # Apply activation function (tanh with chaotic modulation)
                activation = np.tanh(input_val)
                chaotic_mod = 1.0 + 0.1 * np.sin(0.5 * t + i)
                new_states[i] = activation * chaotic_mod
                
                # Add coupling term
                if t > 0:
                    coupling = self.coupling_strengths[i] * (states[i] - new_states[i])**2
                    result += coupling
                    
            states = new_states
            
        # Add polynomial fitness components
        for i in range(self.dim):
            result += (x[i]**4 - 6.0 * x[i]**2 + 4.0 * x[i])**2
            
        # Add multi-scale chaotic modulation
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.3 * np.cos(0.4 * i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
            
        # Add boundary penalty with chaotic scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x[i])
            if dist_from_bound < 0:
                chaotic_scale = 1.0 + 0.2 * np.sin(0.1 * i + 1.0)
                boundary_penalty += 10.0 * np.exp(-dist_from_bound**2 * chaotic_scale)
        result += boundary_penalty
        
        # Add adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * np.sin(0.2 * self.dim) + 0.05 * np.cos(0.1 * self.dim)
        result *= condition_factor
        
        return result