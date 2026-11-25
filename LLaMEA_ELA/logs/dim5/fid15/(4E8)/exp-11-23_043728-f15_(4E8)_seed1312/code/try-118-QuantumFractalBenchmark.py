import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired parameters with fractal scaling
        self.hbar = 1.0
        self.alpha = 0.7
        self.beta = 0.3
        self.gamma = 0.85
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Quantum-like interference pattern using sine and cosine with dynamic phases
        quantum_phase = np.cumsum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Fractal scaling component with multiple resolution levels
        fractal_component = np.zeros(self.dim)
        for i in range(self.dim):
            fractal_component[i] = np.sum([np.sin((2**j) * np.pi * x_norm[i]) * (0.5**j) 
                                         for j in range(1, min(6, int(np.log2(i+2)) + 2))])
        
        # Dynamic coupling between dimensions with adaptive strength
        coupling_strength = 0.4 + 0.3 * np.sin(0.5 * np.arange(self.dim))
        coupled_terms = np.sum(coupling_strength * (x_norm[1:] - x_norm[:-1])**2)
        
        # Quantum harmonic oscillator potential with fractal modulation
        quantum_potential = np.sum((x_norm**2) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)))
        
        # Multi-scale periodic structure with exponential growth in frequency
        periodic_pattern = np.sum([np.sin((2**i) * np.pi * x_norm) * np.cos((3**i) * np.pi * x_norm)
                                  for i in range(min(4, self.dim))])
        
        # Adaptive basin complexity based on dimensionality
        basin_complexity = 0.5 * self.dim * np.mean(np.abs(x_norm - np.mean(x_norm)))
        
        # Fractal scaling factor that increases with dimension
        fractal_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * self.dim**1.3
        
        # Interference pattern combining quantum and fractal components
        interference = np.sum(quantum_phase * fractal_component)
        
        # Combine all components with appropriate weights
        total_energy = (quantum_potential + 
                       0.7 * np.sum(fractal_component**2) + 
                       0.3 * coupled_terms + 
                       0.4 * periodic_pattern**2 + 
                       0.2 * interference**2 +
                       basin_complexity)
        
        # Add ruggedness through small random perturbations
        ruggedness = 0.02 * np.random.rand()
        
        return fractal_scale * (total_energy + ruggedness)