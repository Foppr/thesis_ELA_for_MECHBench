import numpy as np

class QuantumRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters
        self.quantum_angles = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        self.quantum_frequencies = np.random.uniform(1.0, 8.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(20, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=20)
        
        # Adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequencies = np.random.uniform(0.5, 6.0, size=dim)
        self.noise_decay_rates = np.random.uniform(0.1, 0.8, size=dim)
        
        # Oscillation modulation parameters
        self.oscillation_strengths = np.random.uniform(0.5, 2.5, size=dim)
        self.oscillation_phases = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Global scaling and bias
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.global_bias = np.random.uniform(-1.0, 1.0)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillation component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation = self.quantum_amplitudes[i] * np.sin(
                self.quantum_frequencies[i] * x[i] + self.quantum_angles[i]
            )
            quantum_component += oscillation
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(20):
            center = self.rbf_centers[i]
            diff = x - center
            distance_squared = np.sum(diff ** 2)
            rbf_value = self.rbf_widths[i] * np.exp(-distance_squared / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_value
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitudes[i] * np.sin(
                self.noise_frequencies[i] * x[i]
            ) * np.exp(-self.noise_decay_rates[i] * np.abs(x[i]))
            noise_component += noise_val
            
        # Oscillation modulation component
        modulation_component = 0.0
        for i in range(self.dim):
            mod_val = self.oscillation_strengths[i] * np.cos(
                self.oscillation_phases[i] + x[i]
            )
            modulation_component += mod_val
            
        # Combined fitness with weighted components
        return (self.global_scale * (quantum_component**2 + rbf_component) + 
                self.global_bias + 
                0.5 * noise_component + 
                0.3 * modulation_component)