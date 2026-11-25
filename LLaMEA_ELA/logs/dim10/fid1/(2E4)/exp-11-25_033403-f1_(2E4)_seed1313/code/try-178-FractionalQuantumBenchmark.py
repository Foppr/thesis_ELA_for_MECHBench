import numpy as np

class FractionalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractional Brownian motion parameters
        self.hurst_exponent = np.random.uniform(0.1, 0.9, dim)
        self.fractal_scale = np.random.uniform(0.5, 2.0, dim)
        # Quantum harmonic oscillator parameters
        self.oscillator_freq = np.random.uniform(0.5, 3.0, dim)
        self.oscillator_mass = np.random.uniform(0.5, 2.0, dim)
        # Terrain scaling parameters
        self.scaling_factor = np.random.uniform(0.1, 1.0, dim)
        self.terrain_shift = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            # Approximate fractional Brownian motion using random walks with long-range dependence
            pos = (x[i] + 5.0) / 10.0  # Normalize to [0, 1]
            # Use a simple approximation of FBM with Hurst exponent
            fbm_value = np.sin(pos * self.fractal_scale[i] * 2 * np.pi) * \
                       np.exp(-self.hurst_exponent[i] * pos**2)
            fbm_term += fbm_value
            
        # Quantum harmonic oscillator component
        quantum_term = 0.0
        for i in range(self.dim):
            # Harmonic oscillator potential with quantum corrections
            oscillator_energy = 0.5 * self.oscillator_freq[i] * (x[i]**2) + \
                               0.1 * np.sin(x[i] * self.oscillator_freq[i])
            quantum_term += oscillator_energy
            
        # Adaptive terrain scaling component
        terrain_term = 0.0
        for i in range(self.dim):
            # Create adaptive terrain with shifting local minima
            shift = self.terrain_shift[i]
            scale = self.scaling_factor[i]
            terrain_value = (x[i] - shift)**2 * np.exp(-scale * np.abs(x[i] - shift))
            terrain_term += terrain_value
            
        # Cross-dimensional coupling with fractal interference
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal interference pattern between dimensions
                dist = np.abs(x[i] - x[j])
                interference = np.sin(dist * self.oscillator_freq[i]) * \
                              np.cos(dist * self.oscillator_freq[j]) * \
                              np.exp(-0.5 * dist**2)
                coupling_term += interference
                
        # Combine all components with adaptive weights
        total = 0.3 * fbm_term + 0.4 * quantum_term + 0.2 * terrain_term + 0.1 * coupling_term
        
        return total