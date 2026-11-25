import numpy as np

class CrossDimensionalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Exponential barrier functions with position-dependent parameters
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers at different positions
            barrier_positions = [-0.8, -0.4, 0.0, 0.4, 0.8]
            for pos in barrier_positions:
                strength = 2.0 + 1.0 * np.sin(0.7 * i)
                width = 0.3 + 0.2 * np.cos(0.5 * i)
                barriers += strength * np.exp(-0.5 * ((x_scaled[i] - pos) / width)**2)
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomial coupling terms with chaotic modulation
                coeff = 1.0 + 0.5 * np.sin(0.3 * (i + j))
                coupling += coeff * (x_scaled[i]**2) * (x_scaled[j]**3) * \
                           np.sin(0.5 * x_scaled[i] + 0.4 * x_scaled[j])
        
        # Saddle point landscape with hyperbolic tangent components
        saddle = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent terms creating saddle points
            saddle += np.tanh(2.0 * x_scaled[i]) * np.sin(3.0 * x_scaled[i])
        
        # Global scaling and mixing of components
        return 1.5 * periodic + 2.0 * barriers + 1.2 * coupling + 0.8 * saddle