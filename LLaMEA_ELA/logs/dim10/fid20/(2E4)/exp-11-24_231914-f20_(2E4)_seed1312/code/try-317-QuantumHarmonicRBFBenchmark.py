import numpy as np

class QuantumHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters with superposition states
        self.oscillator_freq = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillator_amp = np.random.uniform(1.0, 5.0, size=dim)
        self.oscillator_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial basis function cluster centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        # Temporal gradient flow parameters with time-dependent components
        self.flow_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.flow_frequency = np.random.uniform(0.1, 2.0, size=dim)
        self.flow_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Quantum tunneling probabilities between regions
        self.tunnel_prob = np.random.uniform(0.01, 0.3, size=dim)
        # Multi-scale interference patterns with dynamic amplitudes
        self.interference_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.interference_amp = np.random.uniform(0.5, 4.0, size=dim)
        # Adaptive basin shaping with time-varying depth parameters
        self.basin_depths = np.random.uniform(1.0, 6.0, size=10)
        self.basin_radii = np.random.uniform(0.2, 2.5, size=10)
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=(10, dim))
        # Cross-dimensional coupling with quantum entanglement-like interactions
        self.entanglement_strength = np.random.uniform(0.1, 1.5, size=(dim, dim))
        # Dynamic penalty terms that evolve over time
        self.penalty_strength = np.random.uniform(2.0, 6.0, size=dim)
        self.penalty_decay = np.random.uniform(0.1, 0.8, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freq[i]
            amp = self.oscillator_amp[i]
            phase = self.oscillator_phase[i]
            osc_val = amp * np.sin(freq * x[i] + phase) + amp * np.cos(freq * x[i] + phase)
            quantum_component += osc_val
            
        # Radial basis function cluster component
        rbf_component = 0.0
        for i in range(15):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.rbf_weights[i]
            dist_sq = np.sum((x - center) ** 2)
            rbf_val = weight * np.exp(-dist_sq / (2 * width**2))
            rbf_component += rbf_val
            
        # Temporal gradient flow component
        flow_component = 0.0
        for i in range(self.dim):
            mag = self.flow_magnitude[i]
            freq = self.flow_frequency[i]
            phase = self.flow_phase[i]
            flow_val = mag * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            flow_component += flow_val
            
        # Quantum tunneling component
        tunnel_component = 0.0
        for i in range(self.dim):
            prob = self.tunnel_prob[i]
            tunnel_val = prob * np.sin(x[i]) * np.cos(x[i])
            tunnel_component += tunnel_val
            
        # Interference pattern component
        interference_component = 0.0
        for i in range(self.dim):
            freq = self.interference_freq[i]
            amp = self.interference_amp[i]
            int_val = amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            interference_component += int_val
            
        # Basin shaping component with time-varying depths
        basin_component = 0.0
        for i in range(10):
            center = self.basin_centers[i]
            radius = self.basin_radii[i]
            depth = self.basin_depths[i]
            dist = np.sqrt(np.sum((x - center) ** 2))
            if dist <= radius:
                basin_val = depth * (1 - dist / radius)
                basin_component += basin_val
                
        # Cross-dimensional entanglement component
        entanglement_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    strength = self.entanglement_strength[i, j]
                    ent_val = strength * np.sin(x[i]) * np.cos(x[j])
                    entanglement_component += ent_val
                    
        # Dynamic penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            strength = self.penalty_strength[i]
            decay = self.penalty_decay[i]
            penalty_val = strength * (np.abs(x[i]) ** (1 + decay))
            penalty_component += penalty_val
            
        # Combine all components with appropriate weights
        return (1.2 * quantum_component + 
                1.5 * rbf_component + 
                1.3 * flow_component + 
                0.8 * tunnel_component + 
                1.0 * interference_component + 
                0.9 * basin_component + 
                0.7 * entanglement_component + 
                0.6 * penalty_component)