import numpy as np

class QuantumRadialNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-like oscillation parameters
        self.oscillation_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.oscillation_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillation_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Radial basis function cluster centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 5.0, size=dim)
        self.noise_decay = np.random.uniform(0.1, 0.9, size=dim)
        
        # Quantum tunneling probabilities
        self.tunnel_prob = np.random.uniform(0.01, 0.3, size=dim)
        
        # Dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        
        # Interaction weights between dimensions
        self.interaction_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum oscillation component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation = self.oscillation_amp[i] * np.sin(self.oscillation_freq[i] * x[i] + self.oscillation_phase[i])
            # Add quantum tunneling effect
            if np.random.random() < self.tunnel_prob[i]:
                oscillation += np.random.normal(0, 0.5)
            quantum_component += oscillation
            
        # Radial basis function component with multiple clusters
        rbf_component = 0.0
        for i in range(15):
            center = self.rbf_centers[i]
            diff = x - center
            distance_squared = np.sum(diff**2)
            rbf_value = self.rbf_weights[i] * np.exp(-distance_squared / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_value
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            # Apply decay factor based on distance from center
            decay_factor = np.exp(-self.noise_decay[i] * np.abs(x[i]))
            noise_component += noise_val * decay_factor
            
        # Dimensional interaction component
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_weights[i, j] * x[i] * x[j]
                    
        # Scaling and final combination
        total = (1.2 * quantum_component + 
                1.5 * rbf_component + 
                0.8 * noise_component + 
                0.6 * interaction_component)
        
        return total