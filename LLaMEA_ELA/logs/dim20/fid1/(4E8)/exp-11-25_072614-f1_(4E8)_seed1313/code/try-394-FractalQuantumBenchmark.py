import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyperchaotic fractal-quantum parameters with enhanced complexity
        self.h_bar = 0.2 + 0.3 * np.random.rand()
        self.resonance_freq = 0.8 + 2.2 * np.random.rand()
        self.tunneling_strength = 0.4 + 0.5 * np.random.rand()
        self.fractal_exp = 1.2 + 1.3 * np.random.rand()
        self.coupling_mod = 0.5 + 0.5 * np.random.rand()
        self.memory_decay = 0.2 + 0.3 * np.random.rand()
        self.stochastic_resonance = 0.6 + 0.4 * np.random.rand()
        # Additional chaotic parameters for enhanced landscape complexity
        self.chaos_factor = 0.7 + 0.3 * np.random.rand()
        self.interference_strength = 1.0 + 1.5 * np.random.rand()
        # New hyperchaotic parameters for increased mutation
        self.quantum_phase_shift = 0.5 + 0.5 * np.random.rand()
        self.memory_coupling_range = 12 + np.random.randint(0, 5)
        self.tunnel_barrier_mod = 0.8 + 0.4 * np.random.rand()
        self.basin_adaptivity = 0.3 + 0.7 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperchaotic quantum spectral filtering component
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freq * (1.0 + 0.3 * np.sin(i * 0.4))
            phase = x[i] * freq + np.random.rand() * 2 * np.pi + self.quantum_phase_shift * np.cos(i * 0.3)
            quantum_term += np.sin(phase) * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2)
            
        # Fractal dimension scaling with enhanced hyperchaotic effects
        fractal_scale = np.power(np.sum(np.abs(x)), self.fractal_exp)
        
        # Extended dynamic memory coupling resonance with interference patterns
        coupling_term = 0.0
        memory_weights = np.zeros(self.dim)
        for i in range(self.dim):
            memory_weights[i] = np.exp(-self.memory_decay * i)
            for j in range(i+1, min(i+self.memory_coupling_range, self.dim)):  # Increased coupling range
                coupling_strength = self.coupling_mod * np.sin(0.4 * (i - j)) * memory_weights[j]
                interference = self.interference_strength * np.cos(x[i] * x[j] * 0.5)
                coupling_term += coupling_strength * interference
                
        # Multi-scale tunneling barriers with enhanced stochastic modulation
        tunnel_term = 0.0
        for i in range(self.dim):
            barrier_height = 1.2 + 1.0 * np.sin(i * 0.6) * self.tunnel_barrier_mod
            barrier_width = 0.3 + 0.4 * np.cos(i * 0.4)
            # Enhanced stochastic modulation with chaos factor
            stochastic_mod = 1.0 + 0.4 * np.sin(0.5 * np.sum(x) + i + self.chaos_factor * np.random.rand())
            tunnel_term += barrier_height * stochastic_mod * np.exp(-0.5 * ((x[i] - 1.5 * np.sin(i * 0.4)) / barrier_width)**2)
            
        # Enhanced adaptive quantum potential with memory effects
        potential = 0.0
        for i in range(self.dim):
            potential += (x[i]**2) * (1.0 + 0.4 * np.cos(0.5 * x[i])) * np.exp(-self.memory_decay * i)
            
        # Enhanced time-varying quantum phase with stochastic resonance enhancement
        time_phase = np.sin(0.2 * np.sum(x) + np.random.rand() * 2 * np.pi) * self.stochastic_resonance
        
        # Enhanced basin modulation component for increased discrimination
        basin_mod = 0.0
        for i in range(self.dim):
            basin_mod += np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]) * self.basin_adaptivity
            
        # Additional chaotic interference term for enhanced landscape complexity
        chaos_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                chaos_interference += np.sin(x[i] + x[j]) * np.cos(0.3 * (x[i] - x[j]))
                
        # Additional hyperchaotic cross-dimensional coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x[i] * x[j] * 0.3) * np.cos(0.2 * (x[i] + x[j]))
                
        # Combine all components with enhanced weighting scheme
        result = (quantum_term * fractal_scale + 
                 coupling_term * self.tunneling_strength + 
                 tunnel_term * 0.7 + 
                 potential * 0.5 + 
                 time_phase * 0.3 + 
                 basin_mod * 0.4 + 
                 chaos_interference * 0.2 +
                 cross_coupling * 0.1)
        
        return result