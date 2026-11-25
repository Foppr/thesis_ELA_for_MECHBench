import numpy as np

class HierarchicalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural network parameters
        self.num_layers = max(2, int(np.log2(dim)) + 1)
        self.layer_weights = np.random.uniform(-1.0, 1.0, (self.num_layers, dim))
        self.feedback_delays = np.random.randint(1, 5, self.num_layers)
        self.resonance_frequencies = np.random.uniform(0.1, 2.0, (self.num_layers, dim))
        self.fractal_orders = np.random.uniform(0.3, 1.7, self.num_layers)
        self.adaptive_coupling = np.random.uniform(0.5, 2.0, (self.num_layers, dim))
        # Time-delayed dynamics parameters
        self.delay_weights = np.random.uniform(-0.5, 0.5, (self.num_layers, dim))
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, self.num_layers)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic neural network with time-delayed feedback
        result = 0.0
        previous_states = np.zeros(self.dim)
        
        for layer in range(self.num_layers):
            # Fractional calculus component with varying order
            fractional_term = 0.0
            for i in range(self.dim):
                frac_order = self.fractal_orders[layer]
                # Simplified fractional derivative approximation
                if i > 0:
                    fractional_term += (x_norm[i] - x_norm[i-1])**frac_order
                else:
                    fractional_term += x_norm[i]**frac_order
            
            # Resonance and coupling terms
            resonance = np.sin(self.resonance_frequencies[layer] * x_norm)
            coupling = self.adaptive_coupling[layer] * np.sin(2 * np.pi * (x_norm + previous_states))
            
            # Time-delayed feedback with dynamic weights
            delay_idx = layer % len(self.feedback_delays)
            delayed_input = np.roll(x_norm, self.feedback_delays[delay_idx])
            feedback_term = self.delay_weights[layer] * delayed_input
            
            # Layer activation function (chaotic sigmoid-like)
            layer_output = np.tanh(
                self.layer_weights[layer] * (resonance + coupling + feedback_term) + 
                fractional_term
            )
            
            # Add noise for chaotic behavior
            noise = np.random.normal(0, self.noise_amplitudes[layer], self.dim)
            layer_result = np.sum(layer_output + noise)
            
            # Apply layer-specific scaling
            result += layer_result * np.exp(-0.5 * np.sum(x_norm**2) / (layer + 1))
            
            # Update previous states for next iteration
            previous_states = x_norm.copy()
        
        # Multi-scale chaotic coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling with time-varying strength
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = (1.0 + np.sin(dist * 3)) * \
                                  np.exp(-dist**2 / (2 * (0.5 + 0.5 * np.cos(x_norm[i]))))
                coupling_terms += coupling_strength * np.cos(5 * (x_norm[i] - x_norm[j]))
        
        # Additional chaotic harmonic components
        harmonic_component = 0.0
        for i in range(self.dim):
            # Multiple chaotic sine waves with different frequencies and amplitudes
            harmonic_component += (
                1.2 * np.sin(3 * x_norm[i]) + 
                0.8 * np.cos(5 * x_norm[i]) + 
                0.6 * np.sin(7 * x_norm[i]) + 
                0.4 * np.cos(9 * x_norm[i]) +
                0.2 * np.sin(11 * x_norm[i])
            ) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combine all components with enhanced complexity
        total = result + 0.4 * coupling_terms + 0.3 * harmonic_component
        
        return total