import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with exponential decay
        quadratic = np.sum(x**2 * np.exp(-0.1 * np.abs(x)))
        
        # Trigonometric interactions with varying frequencies
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension interactions
                trig_interaction += np.sin(x[i] * x[j]) * np.cos(2 * x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Fractal-like component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(3 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * x[i]**2) * np.sin(0.5 * np.sum(x**2))
        
        # Chaotic spiral component with radial modulation
        spiral = 0.0
        for i in range(self.dim):
            spiral += np.sin(7 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.15 * x[i]**2) * np.sin(0.3 * np.sum(x**2))
        
        # Exponentially decaying sinusoidal waves
        wave = 0.0
        for i in range(self.dim):
            wave += np.exp(-0.3 * np.abs(x[i])) * np.sin(4 * x[i]) * np.cos(6 * x[i])
        
        # Cross-dimensional polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multimodal component with Gaussian peaks and sinusoidal modulation
        multimodal = 0.0
        centers = np.linspace(-4, 4, 9)
        for c in centers:
            center = np.full(self.dim, c)
            gaussian = np.exp(-0.2 * np.sum((x - center)**2))
            sinusoidal = np.sin(2 * np.sum(x - center))
            multimodal += gaussian * sinusoidal
        
        # Add a component with inverse distance scaling
        inv_distance = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-10)
                inv_distance += np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) / dist
        
        # Add a fractional power component for nonlinearity
        fractional = 0.2 * np.sum(np.abs(x)**1.7 * np.sin(3 * x))
        
        # Add a periodic modulation based on sum of coordinates
        periodic = 0.15 * np.sum(np.sin(2 * np.sum(x)) * np.cos(4 * np.sum(x)) * np.exp(-0.05 * x**2))
        
        # Combine all components with appropriate weights
        return (quadratic + 0.6 * trig_interaction + 0.5 * fractal + 0.4 * spiral + 
                0.3 * wave + 0.2 * poly_interaction + 0.7 * multimodal + 0.1 * inv_distance + 
                0.25 * fractional + 0.15 * periodic)