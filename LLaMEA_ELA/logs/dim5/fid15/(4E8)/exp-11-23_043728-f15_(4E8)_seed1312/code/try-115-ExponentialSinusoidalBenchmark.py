import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential decay and sinusoidal components
        self.alpha = 0.8
        self.beta = 3.0
        self.gamma = 2.2
        self.delta = 0.5
        # Add quantum-inspired parameters
        self.omega = 2.0 * np.pi
        self.phi = np.pi / 4
        # Fractal dimension scaling (increased for more complexity)
        self.fractal_dim = 2.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Exponential decay component with fractal scaling
        exp_decay = np.sum(self.alpha * np.exp(-self.beta * np.power(np.abs(x_norm), self.fractal_dim)))
        
        # Sinusoidal modulation component with quantum interference
        sin_mod = np.sum(np.sin(self.gamma * x_norm + self.phi) * np.cos(self.delta * x_norm + self.omega))
        
        # Gradient-based attraction fields with dynamic coupling
        grad_attraction = 0.0
        for i in range(self.dim - 1):
            grad_attraction += (x_norm[i] - x_norm[i+1])**2 * (1 + 0.2 * np.sin(0.8 * x_norm[i]))
        
        # Multi-modal structure with fractal basin distribution
        modal_structure = 0.0
        for i in range(self.dim):
            term = x_norm[i]**4 - 6 * x_norm[i]**2 + 4 * np.cos(0.9 * x_norm[i])
            modal_structure += term**2
        
        # Quantum interference pattern with enhanced chaos
        quantum_pattern = 0.0
        for i in range(self.dim):
            quantum_pattern += np.sin(self.omega * x_norm[i] + self.phi) * np.cos(self.omega * x_norm[i] + self.phi)
        
        # Dynamic dimension coupling with enhanced chaotic behavior
        coupling_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling_term += np.sin(x_norm[i] * x_norm[i+1]) * (1 + 0.4 * np.cos(3.0 * x_norm[i]))
        
        # Add fractal basin complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            basin_complexity += np.sin(2.5 * x_norm[i]) * np.cos(1.5 * x_norm[i]) * (1 + 0.15 * np.sin(3.0 * x_norm[i]))
        
        # Combine all components with adaptive weighting and fractal energy distribution
        total_energy = exp_decay + 0.4 * sin_mod + 0.3 * grad_attraction + 0.6 * modal_structure + 0.15 * quantum_pattern + 0.2 * coupling_term + 0.1 * basin_complexity
        
        # Add chaotic noise for ruggedness with better statistical properties
        noise = 0.008 * np.random.rand() * (1 + 0.3 * np.sin(np.sum(x_norm**2)))
        
        return total_energy + noise