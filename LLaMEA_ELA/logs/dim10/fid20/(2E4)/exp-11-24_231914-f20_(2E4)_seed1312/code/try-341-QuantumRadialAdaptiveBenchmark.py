import numpy as np

class QuantumRadialAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired oscillation parameters
        self.oscillation_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.oscillation_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillation_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        
        # Adaptive terrain scaling factors
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        self.adaptation_rate = np.random.uniform(0.1, 0.5, size=dim)
        
        # Quantum tunneling parameters
        self.tunnel_prob = np.random.uniform(0.01, 0.3, size=dim)
        self.tunnel_strength = np.random.uniform(1.0, 5.0, size=dim)
        
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(0.5, 8.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.3, 2.5, size=dim)
        
        # Basin interaction parameters
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=(8, dim))
        self.basin_radii = np.random.uniform(0.5, 2.5, size=8)
        self.basin_depths = np.random.uniform(1.0, 6.0, size=8)
        
        # Dynamic fitness modulation
        self.modulation_freq = np.random.uniform(0.1, 1.0, size=dim)
        self.modulation_amp = np.random.uniform(0.1, 1.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum oscillation component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation = self.oscillation_amp[i] * np.sin(self.oscillation_freq[i] * x[i] + self.oscillation_phase[i])
            # Add quantum tunneling effect
            if np.random.random() < self.tunnel_prob[i]:
                oscillation += self.tunnel_strength[i] * np.random.normal(0, 1)
            quantum_component += oscillation
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i])**2)
            rbf_component += np.exp(-dist / (2 * self.rbf_widths[i]**2))
            
        # Adaptive terrain scaling
        adaptive_component = 0.0
        for i in range(self.dim):
            adaptive_component += self.scaling_factors[i] * x[i]**2
            
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_component += self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * x[i])
            
        # Basin interaction component
        basin_component = 0.0
        for i in range(8):
            dist = np.sqrt(np.sum((x - self.basin_centers[i])**2))
            if dist <= self.basin_radii[i]:
                basin_component += self.basin_depths[i] * (1 - dist / self.basin_radii[i])
                
        # Dynamic modulation component
        modulation_component = 0.0
        for i in range(self.dim):
            modulation_component += self.modulation_amp[i] * np.cos(self.modulation_freq[i] * x[i])
            
        # Combine all components with appropriate weights
        return (2.0 * quantum_component + 
                1.5 * rbf_component + 
                1.2 * adaptive_component + 
                1.0 * harmonic_component + 
                0.8 * basin_component + 
                0.5 * modulation_component)