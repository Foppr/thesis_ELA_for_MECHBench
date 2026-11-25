import numpy as np

class QuantumFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quantum fractal parameters
        self.h_bar = 0.5 + 0.5 * np.random.rand()
        self.resonance_freq = 1.0 + 2.0 * np.random.rand()
        self.tunneling_strength = 0.1 + 0.4 * np.random.rand()
        self.fractal_exp = 1.2 + 0.6 * np.random.rand()
        self.coupling_mod = 0.5 + 0.5 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum spectral filtering component
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freq * (1.0 + 0.3 * np.sin(i * 0.5))
            phase = x[i] * freq + np.random.rand() * 2 * np.pi
            quantum_term += np.sin(phase) * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2)
            
        # Fractal dimension scaling with quantum effects
        fractal_scale = np.power(np.sum(np.abs(x)), self.fractal_exp)
        
        # Dynamic coupling resonance
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                coupling_strength = self.coupling_mod * np.sin(0.2 * (i - j))
                coupling_term += coupling_strength * np.cos(x[i] * x[j])
                
        # Tunneling barrier component with multi-scale structure
        tunnel_term = 0.0
        for i in range(self.dim):
            barrier_height = 1.0 + 0.5 * np.sin(i * 0.8)
            barrier_width = 0.3 + 0.2 * np.cos(i * 0.6)
            tunnel_term += barrier_height * np.exp(-0.5 * ((x[i] - 1.5 * np.sin(i * 0.4)) / barrier_width)**2)
            
        # Adaptive quantum potential
        potential = 0.0
        for i in range(self.dim):
            potential += (x[i]**2) * (1.0 + 0.2 * np.cos(0.3 * x[i]))
            
        # Time-varying quantum phase
        time_phase = np.sin(0.1 * np.sum(x) + np.random.rand() * 2 * np.pi)
        
        # Combine all components with quantum-inspired weighting
        result = (quantum_term * fractal_scale + 
                 coupling_term * self.tunneling_strength + 
                 tunnel_term * 0.7 + 
                 potential * 0.3 + 
                 time_phase * 0.1)
        
        return result