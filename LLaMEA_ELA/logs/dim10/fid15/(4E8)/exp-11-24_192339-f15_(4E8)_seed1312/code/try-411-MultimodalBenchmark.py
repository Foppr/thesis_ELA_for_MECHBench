import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with quantum-like interference and memory effects
        chaos = 0
        memory = np.zeros(self.dim)
        for i in range(self.dim):
            degree = 3 + int(np.abs(x[i]) * 0.7) % 5
            poly_term = np.sum([np.power(x[i], k) * np.sin(k * x[i]) for k in range(1, degree + 1)])
            chaos += poly_term * np.exp(-0.15 * x[i]**2)
            memory[i] = np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
        
        # Modified radial basis function with quantum harmonic modulation and stochastic resonance
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            width = 0.3 + 0.4 * np.sin(0.5 * x[i] + np.pi/4)
            # Add stochastic resonance component
            noise = np.random.normal(0, 0.05)
            for center in centers:
                rbf += np.exp(-0.3 * ((x[i] - center) / width)**2) * np.cos(0.2 * x[i]) * (1 + noise)
        
        # Enhanced chaotic gradient coupling with fractal scaling and memory-dependent dynamics
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Memory-dependent interaction
                mem_i = memory[i] if i < len(memory) else 0
                mem_j = memory[j] if j < len(memory) else 0
                coupling += np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(0.5 * (x[i] + x[j])) * (1 + 0.1 * mem_i * mem_j)
        
        # Quantum-inspired oscillatory components with multi-scale interference and dynamic phase
        oscillation = 0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.6 * x[i])
            scale = 1.2 + 0.3 * np.cos(0.7 * x[i])
            # Add dynamic phase modulation
            phase = 0.1 * np.sin(0.5 * x[i]) * memory[i] if i < len(memory) else 0
            oscillation += scale * np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive fractal basin structure with dynamic saddle points and memory effects
        basin = 0
        for i in range(self.dim):
            transition = 1.0 / (1.0 + np.exp(-3.0 * (x[i] - 2.0)))
            # Add memory-dependent basin modification
            mem_mod = 1.0 + 0.2 * memory[i] if i < len(memory) else 1.0
            basin += transition * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1) * mem_mod
        
        # Additional chaotic ridge structures with dynamic curvature and memory influence
        ridge = 0
        for i in range(self.dim):
            # Dynamic curvature based on memory
            curv = 1.0 + 0.3 * memory[i] if i < len(memory) else 1.0
            ridge += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.05 * x[i]**2) * curv
        
        # Add stochastic noise to overall function for enhanced complexity
        total = 0.22 * chaos + 0.23 * rbf + 0.18 * coupling + 0.22 * oscillation + 0.12 * basin + 0.03 * ridge
        noise = np.random.normal(0, 0.05)
        
        return total + noise