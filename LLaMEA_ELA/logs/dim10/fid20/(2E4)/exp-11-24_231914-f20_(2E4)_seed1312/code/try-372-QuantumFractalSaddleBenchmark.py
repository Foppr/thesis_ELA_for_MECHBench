import numpy as np

class QuantumFractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired oscillator parameters
        self.oscillator_freq = np.random.uniform(0.5, 5.0, size=dim)
        self.oscillator_amp = np.random.uniform(0.1, 2.0, size=dim)
        self.oscillator_phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_coeff = np.random.uniform(0.5, 2.0, size=dim)
        
        # Fractional Brownian motion parameters for fractal structure
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fractal_scale = np.random.uniform(0.5, 3.0, size=dim)
        
        # Saddle-point region parameters
        self.saddle_centers = np.random.uniform(-4.0, 4.0, size=(5, dim))
        self.saddle_strength = np.random.uniform(1.0, 5.0, size=5)
        self.saddle_width = np.random.uniform(0.5, 2.0, size=5)
        
        # Time-varying topology parameters
        self.time_freq = np.random.uniform(0.1, 0.5, size=dim)
        self.time_amp = np.random.uniform(0.1, 1.0, size=dim)
        self.topology_shift = np.random.uniform(-0.5, 0.5, size=dim)
        
        # Multi-modal peak parameters
        self.peak_centers = np.random.uniform(-4.5, 4.5, size=(8, dim))
        self.peak_heights = np.random.uniform(2.0, 8.0, size=8)
        self.peak_widths = np.random.uniform(0.3, 1.5, size=8)
        
        # Coupling and interaction terms
        self.coupling_strength = np.random.uniform(0.1, 1.0, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillation = self.oscillator_amp[i] * np.sin(self.oscillator_freq[i] * x[i] + self.oscillator_phase[i])
            quantum_component += self.quantum_coeff[i] * oscillation
        
        # Fractional Brownian motion fractal component
        fractal_component = 0.0
        for i in range(self.dim):
            # Simplified fractal approximation using harmonic series
            fbm_val = 0.0
            for k in range(1, 6):
                freq = (k + 1) * self.fractal_scale[i]
                amp = (1.0 / (k ** (2.0 - self.hurst[i]))) * np.sin(freq * x[i])
                fbm_val += amp
            fractal_component += fbm_val
        
        # Saddle-point regions with dynamic topology
        saddle_component = 0.0
        for i in range(5):
            dist = np.sum((x - self.saddle_centers[i]) ** 2)
            if dist < self.saddle_width[i] ** 2:
                saddle_component += self.saddle_strength[i] * np.exp(-dist / (2 * self.saddle_width[i] ** 2))
        
        # Time-varying topology component
        time_component = 0.0
        for i in range(self.dim):
            time_val = self.time_amp[i] * np.sin(self.time_freq[i] * x[i])
            time_component += time_val
        
        # Multi-modal peak component
        peak_component = 0.0
        for i in range(8):
            dist = np.sum((x - self.peak_centers[i]) ** 2)
            peak_component += self.peak_heights[i] * np.exp(-dist / (2 * self.peak_widths[i] ** 2))
        
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_strength[i, j] * x[i] * x[j]
        
        # Combined function with weighted components
        return (2.0 * quantum_component + 
                1.5 * fractal_component + 
                1.8 * saddle_component + 
                1.2 * time_component + 
                1.4 * peak_component + 
                0.8 * coupling_component)