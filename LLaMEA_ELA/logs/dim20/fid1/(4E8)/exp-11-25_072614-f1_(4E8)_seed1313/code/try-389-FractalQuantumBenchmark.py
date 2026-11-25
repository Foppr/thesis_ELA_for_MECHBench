import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyperchaotic fractal-quantum parameters with enhanced complexity
        self.h_bar = 0.3 + 0.7 * np.random.rand()
        self.resonance_freq = 0.5 + 3.0 * np.random.rand()
        self.tunneling_strength = 0.2 + 0.6 * np.random.rand()
        self.fractal_exp = 1.5 + 1.0 * np.random.rand()
        self.coupling_mod = 0.3 + 0.7 * np.random.rand()
        self.memory_decay = 0.1 + 0.4 * np.random.rand()
        self.stochastic_resonance = 0.8 + 0.2 * np.random.rand()
        # New parameters for enhanced discrimination
        self.interference_strength = 0.5 + 1.5 * np.random.rand()
        self.temporal_oscillation = 0.2 + 0.8 * np.random.rand()
        self.basin_complexity = 0.4 + 0.6 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperchaotic quantum spectral filtering component
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freq * (1.0 + 0.5 * np.sin(i * 0.3))
            phase = x[i] * freq + np.random.rand() * 2 * np.pi
            # Add enhanced interference patterns
            interference = np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            quantum_term += (np.sin(phase) + interference) * np.exp(-0.5 * (x[i] / (1.0 + 0.2 * i))**2)
            
        # Fractal dimension scaling with hyperchaotic effects
        fractal_scale = np.power(np.sum(np.abs(x)), self.fractal_exp)
        
        # Enhanced dynamic memory coupling resonance with extended range
        coupling_term = 0.0
        memory_weights = np.zeros(self.dim)
        for i in range(self.dim):
            memory_weights[i] = np.exp(-self.memory_decay * i)
            # Extended coupling range with interference modulation
            for j in range(i+1, min(i+8, self.dim)):  
                coupling_strength = self.coupling_mod * np.sin(0.3 * (i - j)) * memory_weights[j]
                # Add interference pattern to coupling
                interference_pattern = self.interference_strength * np.cos(0.4 * (x[i] + x[j]))
                coupling_term += coupling_strength * np.cos(x[i] * x[j]) * interference_pattern
                
        # Enhanced multi-scale tunneling barriers with stochastic modulation
        tunnel_term = 0.0
        for i in range(self.dim):
            barrier_height = 1.5 + 0.8 * np.sin(i * 0.7)
            barrier_width = 0.2 + 0.3 * np.cos(i * 0.5)
            # Add temporal oscillation to barrier structure
            temporal_mod = 1.0 + self.temporal_oscillation * np.sin(0.4 * np.sum(x) + i + np.sin(i * 0.2))
            tunnel_term += barrier_height * temporal_mod * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(i * 0.3)) / barrier_width)**2)
            
        # Enhanced adaptive quantum potential with memory effects
        potential = 0.0
        for i in range(self.dim):
            # Add complexity to potential function
            potential += (x[i]**2) * (1.0 + 0.3 * np.cos(0.4 * x[i])) * np.exp(-self.memory_decay * i) * (1.0 + 0.2 * np.sin(0.6 * x[i]))
            
        # Enhanced time-varying quantum phase with stochastic resonance enhancement
        time_phase = np.sin(0.15 * np.sum(x) + np.random.rand() * 2 * np.pi) * self.stochastic_resonance
        
        # Enhanced basin modulation component for increased discrimination
        basin_mod = 0.0
        for i in range(self.dim):
            # Add complexity to basin modulation
            basin_mod += (np.sin(0.6 * x[i]) * np.cos(0.4 * x[i]) + 
                         self.basin_complexity * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i]))
            
        # Combine all components with enhanced weighting scheme
        result = (quantum_term * fractal_scale + 
                 coupling_term * self.tunneling_strength + 
                 tunnel_term * 0.8 + 
                 potential * 0.4 + 
                 time_phase * 0.2 + 
                 basin_mod * 0.3)
        
        return result