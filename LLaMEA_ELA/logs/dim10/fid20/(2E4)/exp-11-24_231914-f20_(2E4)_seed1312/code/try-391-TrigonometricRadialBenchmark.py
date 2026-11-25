import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Oscillation parameters for trigonometric components
        self.omega = np.random.uniform(1.0, 10.0, size=dim)
        self.phi = np.random.uniform(0, 2*np.pi, size=dim)
        self.amplitude = np.random.uniform(0.5, 3.0, size=dim)
        
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, size=10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=10)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 3.0, size=dim)
        
        # Cross-dimensional interaction coefficients
        self.interaction_strength = np.random.uniform(0.1, 2.0, size=(dim, dim))
        
        # Scaling factors for different dimensions
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        
        # Periodic modulation parameters
        self.modulation_freq = np.random.uniform(0.1, 1.5, size=dim)
        self.modulation_amp = np.random.uniform(0.2, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric oscillation component
        trig_component = 0.0
        for i in range(self.dim):
            trig_val = self.amplitude[i] * np.sin(self.omega[i] * x[i] + self.phi[i])
            trig_component += trig_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_weights[i] * np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Cross-dimensional interaction component
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_strength[i, j] * x[i] * x[j]
                    
        # Scaling component
        scale_component = 0.0
        for i in range(self.dim):
            scale_val = self.scale_factors[i] * (x[i] ** 2)
            scale_component += scale_val
            
        # Periodic modulation component
        modulation_component = 0.0
        for i in range(self.dim):
            mod_val = self.modulation_amp[i] * np.cos(self.modulation_freq[i] * x[i])
            modulation_component += mod_val
            
        # Combine all components with appropriate weights
        return (1.5 * trig_component + 
                1.2 * rbf_component + 
                0.8 * noise_component + 
                0.6 * interaction_component + 
                0.4 * scale_component + 
                0.3 * modulation_component)