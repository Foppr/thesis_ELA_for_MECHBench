import numpy as np

class QuantumRadialTunnelBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired oscillation parameters
        self.omega = np.random.uniform(0.5, 3.0, size=dim)
        self.phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.amplitude = np.random.uniform(0.5, 2.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.3, 2.0, size=15)
        
        # Stochastic tunneling parameters
        self.tunnel_prob = np.random.uniform(0.01, 0.2, size=dim)
        self.tunnel_strength = np.random.uniform(0.1, 1.0, size=dim)
        self.tunnel_range = np.random.uniform(1.0, 3.0, size=dim)
        
        # Dynamic scaling and rotation components
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        self.rotation_angles = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Multi-frequency harmonic components
        self.harmonic_freqs = np.random.uniform(1.0, 8.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.3, 1.5, size=dim)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 0.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillation component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation = self.amplitude[i] * np.sin(self.omega[i] * x[i] + self.phase[i])
            quantum_component += oscillation
        
        # Radial basis function component with multiple centers
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Stochastic tunneling effect
        tunnel_component = 0.0
        for i in range(self.dim):
            if np.random.random() < self.tunnel_prob[i]:
                tunnel_direction = np.random.choice([-1, 1])
                tunnel_distance = np.random.exponential(self.tunnel_range[i])
                tunnel_component += self.tunnel_strength[i] * tunnel_distance * tunnel_direction
                
        # Dynamic scaling and rotation
        scale_component = 0.0
        for i in range(self.dim):
            scaled_x = x[i] * self.scale_factors[i]
            rotated_x = scaled_x * np.cos(self.rotation_angles[i]) - x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            scale_component += rotated_x ** 2
            
        # Multi-frequency harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * x[i])
            harmonic_component += harmonic_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Combined fitness function
        return (1.2 * quantum_component + 
                1.5 * rbf_component + 
                0.8 * tunnel_component + 
                1.0 * scale_component + 
                0.9 * harmonic_component + 
                0.7 * noise_component)