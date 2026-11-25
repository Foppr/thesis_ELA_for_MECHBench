import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Chaotic gradient field with periodic attractors
        chaotic = 0
        for i in range(self.dim):
            # Periodic chaotic function with multiple attractor points
            attractor1 = np.sin(3.0 * x[i]) * np.exp(-0.5 * (x[i] - 1.0)**2)
            attractor2 = np.cos(2.5 * x[i]) * np.exp(-0.3 * (x[i] + 2.0)**2)
            attractor3 = np.sin(4.0 * x[i]) * np.exp(-0.7 * (x[i] - 3.0)**2)
            
            # Combine attractors with dynamic weights
            weight1 = 1.0 + 0.5 * np.sin(0.2 * i)
            weight2 = 1.0 + 0.3 * np.cos(0.1 * i)
            weight3 = 1.0 + 0.4 * np.sin(0.15 * i)
            
            chaotic += (weight1 * attractor1 + 
                       weight2 * attractor2 + 
                       weight3 * attractor3) * 0.5
            
        # Saddle-point landscape with ridge structures
        saddle = 0
        for i in range(self.dim):
            # Create saddle points with varying curvature
            curvature = 1.0 + 0.2 * np.sin(0.5 * i)
            saddle += (curvature * x[i]**4 - 2 * curvature * x[i]**2) * 0.3
            
        # High-frequency oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            # Add high frequency modulation with amplitude scaling
            freq = 10.0 + 5.0 * np.sin(0.3 * i)
            amp = 1.0 + 0.3 * np.cos(0.2 * i)
            oscillatory += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimension coupling with chaotic interaction
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                # Chaotic coupling term with varying strength
                strength = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                coupling += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like scaling component
        fractal = 0
        for i in range(self.dim):
            # Multi-scale fractal behavior with self-similarity
            scale1 = np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.5 * x[i]**2)
            scale2 = np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.3 * x[i]**2)
            fractal += (scale1 + scale2) * 0.4
            
        # Add a new component: asymmetric gradient flow with momentum-like effects
        momentum = 0
        for i in range(self.dim):
            # Asymmetric function that creates directional bias
            asymmetry = np.tanh(2.0 * x[i]) * np.exp(-0.2 * (x[i] - 1.5)**2)
            momentum += asymmetry * (1.0 + 0.2 * np.sin(0.4 * i))
            
        # Combine all components with different scaling factors
        return (quadratic + 
                chaotic * 0.6 + 
                saddle * 0.3 + 
                oscillatory * 0.8 + 
                coupling * 0.5 + 
                fractal * 0.4 + 
                momentum * 0.2)