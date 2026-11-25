import numpy as np

class FractalQuantumRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fractal_amplitude = np.random.uniform(1.0, 5.0, size=dim)
        self.fractal_frequency = np.random.uniform(0.5, 3.0, size=dim)
        
        # Quantum phase modulation parameters
        self.quantum_phase_amp = np.random.uniform(0.5, 2.0, size=dim)
        self.quantum_phase_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.quantum_phase_offset = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Adaptive ridge parameters
        self.ridge_strength = np.random.uniform(0.5, 3.0, size=dim)
        self.ridge_width = np.random.uniform(0.1, 1.0, size=dim)
        self.ridge_orientation = np.random.uniform(-np.pi, np.pi, size=dim)
        
        # Cross-dimensional interaction coefficients
        self.cross_dim_coupling = np.random.uniform(0.1, 2.0, size=(dim, dim))
        
        # Noise and perturbation parameters
        self.noise_level = np.random.uniform(0.01, 0.5, size=dim)
        self.perturbation_freq = np.random.uniform(0.1, 1.0, size=dim)
        
        # Dimensional scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs
        x_norm = x / 5.0
        
        # Fractal Brownian motion component
        fbm_component = 0.0
        for i in range(self.dim):
            # Simple fractal-like contribution using scaled sinusoids
            fbm_val = 0.0
            for k in range(1, 6):  # Sum of multiple frequency components
                freq = self.fractal_frequency[i] * (2 ** k)
                amp = self.fractal_amplitude[i] / (2 ** (k * self.hurst[i]))
                fbm_val += amp * np.sin(freq * x_norm[i])
            fbm_component += fbm_val
            
        # Quantum phase modulation component
        quantum_component = 0.0
        for i in range(self.dim):
            phase = self.quantum_phase_freq[i] * x_norm[i] + self.quantum_phase_offset[i]
            quantum_val = self.quantum_phase_amp[i] * np.sin(phase) * np.cos(phase)
            quantum_component += quantum_val
            
        # Adaptive ridge structure
        ridge_component = 0.0
        for i in range(self.dim):
            # Ridge along a rotated direction
            ridge_dir = np.array([np.cos(self.ridge_orientation[i]), np.sin(self.ridge_orientation[i])])
            pos_proj = x_norm[i] * ridge_dir[0] + (x_norm[(i+1) % self.dim] if self.dim > 1 else 0) * ridge_dir[1]
            
            # Ridge function with adaptive width and strength
            ridge_val = self.ridge_strength[i] * np.exp(-0.5 * ((pos_proj / self.ridge_width[i]) ** 2))
            ridge_component += ridge_val
            
        # Cross-dimensional coupling
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.cross_dim_coupling[i, j] * x_norm[i] * x_norm[j]
                    
        # Noise and perturbation
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_level[i] * np.sin(self.perturbation_freq[i] * x_norm[i])
            noise_component += noise_val
            
        # Dimensional scaling effects
        scale_component = 0.0
        for i in range(self.dim):
            scale_val = self.scale_factors[i] * (x_norm[i] ** 2)
            scale_component += scale_val
            
        # Combine all components with appropriate weights
        total = (1.5 * fbm_component + 
                1.3 * quantum_component + 
                1.2 * ridge_component + 
                0.8 * coupling_component + 
                0.6 * noise_component + 
                0.4 * scale_component)
                
        return total