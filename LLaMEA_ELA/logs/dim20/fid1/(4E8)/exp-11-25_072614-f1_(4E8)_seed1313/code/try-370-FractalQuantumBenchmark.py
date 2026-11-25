import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyperchaotic quantum fractal parameters
        self.h_bar = 0.3 + 0.7 * np.random.rand()
        self.resonance_freq = 0.5 + 3.0 * np.random.rand()
        self.tunneling_strength = 0.2 + 0.6 * np.random.rand()
        self.fractal_exp = 1.5 + 0.8 * np.random.rand()
        self.coupling_mod = 0.3 + 0.7 * np.random.rand()
        self.memory_decay = 0.1 + 0.4 * np.random.rand()
        self.stochastic_resonance = 0.6 + 0.4 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic quantum spectral filtering component
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freq * (1.0 + 0.5 * np.sin(i * 0.7))
            phase = x[i] * freq + np.random.rand() * 2 * np.pi
            quantum_term += np.sin(phase) * np.exp(-0.3 * (x[i] / (1.0 + 0.2 * i))**2)
            
        # Fractal dimension scaling with hyperchaotic effects
        fractal_scale = np.power(np.sum(np.abs(x)), self.fractal_exp)
        
        # Dynamic memory coupling resonance
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling range
                coupling_strength = self.coupling_mod * np.sin(0.3 * (i - j)) * np.exp(-self.memory_decay * (i-j)**2)
                coupling_term += coupling_strength * np.cos(x[i] * x[j])
                
        # Multi-scale tunneling barriers with stochastic modulation
        tunnel_term = 0.0
        for i in range(self.dim):
            barrier_height = 1.5 + 0.8 * np.sin(i * 0.9)
            barrier_width = 0.2 + 0.3 * np.cos(i * 0.5)
            tunnel_term += barrier_height * np.exp(-0.4 * ((x[i] - 2.0 * np.sin(i * 0.6)) / barrier_width)**2)
            
        # Adaptive quantum potential with memory effects
        potential = 0.0
        for i in range(self.dim):
            potential += (x[i]**2) * (1.0 + 0.3 * np.cos(0.4 * x[i])) * (1.0 + self.stochastic_resonance * np.sin(i * 0.3))
            
        # Time-varying quantum phase with chaotic modulation
        time_phase = np.sin(0.15 * np.sum(x) + np.random.rand() * 2 * np.pi)
        
        # Hyperchaotic basin modulation
        basin_mod = 1.0 + 0.2 * np.sin(np.sum(x) * 0.5)
        
        # Combine all components with enhanced weighting
        result = (quantum_term * fractal_scale * basin_mod + 
                 coupling_term * self.tunneling_strength + 
                 tunnel_term * 0.8 + 
                 potential * 0.4 + 
                 time_phase * 0.15)
        
        return result